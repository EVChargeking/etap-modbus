import struct
from pymodbus.client import ModbusTcpClient


class modbus_wrapper:
    def __init__(self, ip, port=502, slave_id=1):
        self.client = ModbusTcpClient(ip, port)
        self.slave_id = int(slave_id)

    def read(self, address, count):
        try:
            result = self.client.read_holding_registers(address, count, unit=1, slave=self.slave_id)
            return result.registers
        except:
            return None

    def write(self, address, value):
        try:
            result = self.client.write_register(address, value, unit=1, slave=self.slave_id)
            return result
        except:
            return None
    
    def read(self, address, count, data_type):
        res = self.read(address, count)
        if res is None:
            return None
        data_type = str(data_type).upper()
        
        if data_type == "INT16":
            if len(res) != 1:
                return None
            return struct.unpack('>h', struct.pack('>H', res[0]))[0]
        
        elif data_type == "UINT16":
            if len(res) != 1:
                return None
            return struct.unpack('>H', struct.pack('>H', res[0]))[0]
        
        elif data_type == "UINT32":
            if len(res) != 2:
                return None
            return struct.unpack('>I', struct.pack('>HH', res[1], res[0]))[0]
        
        elif data_type == "UINT64":
            if len(res) != 4:
                return None
            return struct.unpack('>Q', struct.pack('>HHHH', res[3], res[2], res[1], res[0]))[0]
        
        elif data_type == "FLOAT":
            if len(res) != 2:
                return None
            return struct.unpack('>f', struct.pack('>HH', res[1], res[0]))[0]
        
        elif data_type == "STRING":
            res = [x.to_bytes(2, byteorder='little') for x in res]
            try:
                return b''.join(res).decode('utf-8')
            except:
                return None
        
        return None

    def close(self):
        self.client.close()
        return

class etap_pro:
    def __init__(self, ip):
        self.modbus_settings = modbus_wrapper(ip=ip, port=502, slave_id=200)
        self.modbus_status = modbus_wrapper(ip=ip, port=502, slave_id=1)
    
    def get_name(self):
        return self.modbus_settings.read(100, 17, "string")
    
    def get_manufacturer(self):
        return self.modbus_settings.read(117, 5, "string")
    
    def get_modbus_version(self):
        return self.modbus_settings.read(122, 5, "int16")
    
    def get_serial_number(self):
        return self.modbus_settings.read(157, 11, "string")
    
if __name__ == "__main__":
    etap = etap_pro(ip="192.168.1.94")
    
    device_name = etap.get_name()
    if device_name is None:
        print("Device not found")
        exit()
    
    print("Found device: " + etap.get_name())
    print("Manufacturer: " + etap.get_manufacturer())
    print("Modbus version: " + str(etap.get_modbus_version()))
    print("Serial number: " + etap.get_serial_number())
    etap.close()