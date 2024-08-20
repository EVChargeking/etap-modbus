import struct
import datetime
import time
from pymodbus.client import ModbusTcpClient


class modbus_wrapper:
    def __init__(self, ip, port=502, slave_id=1):
        self.client = ModbusTcpClient(host=ip, port=port)
        self.slave_id = int(slave_id)

    def _read(self, address, count):
        try:
            result = self.client.read_holding_registers(address=address, count=count, slave=self.slave_id)
            if result.isError():
                return None
            return result.registers
        except:
            return None

    def _write(self, address, value):
        try:
            result = self.client.write_registers(address=address, values=value, slave=self.slave_id)
            return not result.isError()
        except:
            return False
    
    def read(self, address, count, data_type):
        res = self._read(address, count)
        if res is None:
            print("Error reading data")
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
    
    def write(self, address, value, data_type):
        data_type = str(data_type).upper()
        if data_type == "INT16":
            if value < -32768 or value > 32767 or type(value) is not int:
                raise ValueError("Cannot write {0} as INT16".format(value))
            data_to_write = struct.unpack('>H', struct.pack('>h', value))[0]
        elif data_type == "UINT16":
            if value < 0 or value > 65535 or type(value) is not int:
                raise ValueError("Cannot write {0} as UINT16".format(value))
            data_to_write = struct.unpack('>H', struct.pack('>H', value))[0]
        elif data_type == "UINT32":
            if value < 0 or value > 4294967295 or type(value) is not int:
                raise ValueError("Cannot write {0} as UINT32".format(value))
            data_to_write = list(struct.unpack('>HH', struct.pack('>I', value)))
            data_to_write.reverse()
        elif data_type == "UINT64":
            if type(value) is not int:
                raise ValueError("Cannot write {0} as UINT64".format(value))
            data_to_write = list(struct.unpack('>HHHH', struct.pack('>Q', value)))
            data_to_write.reverse()
        elif data_type == "FLOAT":
            try:
                float(value)
            except:
                raise ValueError("Cannot write {0} as FLOAT".format(value))
            data_to_write = list(struct.unpack('>HH', struct.pack('>f', value)))
            data_to_write.reverse()
        elif data_type == "STRING":
            raise ValueError("Cannot write string data")
        else:
            raise ValueError("Invalid data type")
        
        return self._write(address, data_to_write)     

    def close(self):
        self.client.close()
        return

class etap_pro:
    def __init__(self, ip):
        self.modbus_settings = modbus_wrapper(ip=ip, port=502, slave_id=1)
    
    def set_ip(self, ip):
        self.modbus_settings.client.host = ip
    
    def get_name(self):
        return self.modbus_settings.read(100, 17, "string")
    
    def get_manufacturer(self):
        return self.modbus_settings.read(117, 5, "string")
    
    def get_modbus_version(self):
        return self.modbus_settings.read(122, 1, "int16")
    
    def get_serial_number(self):
        return self.modbus_settings.read(157, 11, "string")
    
    def get_time(self):
        time = [] # [year, month, day, hour, minute, second]
        for reg in range(168, 174):
            time.append(self.modbus_settings.read(reg, 1, "int16"))
        if None in time:
            return None
        return datetime.datetime(time[0], time[1], time[2], time[3], time[4], time[5])
    
    def get_voltage(self, line):
        if line < 1 or line > 3:
            return None
        retval = self.modbus_settings.read(306 + ((line - 1)*2), 2, "float")
        if retval is None:
            return None
        return round(retval, 3)
    
    def get_current(self, line):
        if line < 1 or line > 3:
            return None
        retval = self.modbus_settings.read(320 + ((line - 1)*2), 2, "float")
        if retval is None:
            return None
        return round(retval, 3)
    
    def get_board_temperature(self):
        retval = self.modbus_settings.read(1102, 2, "float")
        if retval is None:
            return None
        return round(retval, 3)
    
    def get_ev_plug_temperature(self):
        retval =  self.modbus_settings.read(1106, 2, "float")
        if retval is None:
            return None
        return round(retval, 3)
    
    def get_grid_plug_temperature(self):
        retval = self.modbus_settings.read(1108, 2, "float")
        if retval is None:
            return None
        return round(retval, 3)
    
    def get_max_current(self):
        retval = self.modbus_settings.read(1206, 2, "float")
        if retval is None:
            return None
        return round(retval, 3)
    
    def get_mode(self):
        return self.modbus_settings.read(1201, 5, "string")
    
    def get_mode_int(self):
        return self.modbus_settings.read(1208, 1, "int16")
    
    def get_current_setpoint(self):
        retval = self.modbus_settings.read(1210, 2, "float")
        if retval is None:
            return None
        return round(retval, 3)
    
    def set_current_setpoint(self, current):
        return self.modbus_settings.write(1210, current, "float")
    
    def close(self):
        self.modbus_settings.close()
        return
    
if __name__ == "__main__":
    #etap = etap_pro(ip="e-TAP_Pro_a3eab8.local")
    etap = etap_pro(ip="192.168.88.39")
    
    
    device_name = etap.get_name()
    if device_name is None:
        print("Device not found")
        exit()
    
    print("Found device: " + device_name)
    # print("Manufacturer: " + etap.get_manufacturer())
    # print("Modbus version: " + str(etap.get_modbus_version()))
    print("Serial number: " + etap.get_serial_number())
    # print("Time: " + str(etap.get_time()))
    print("Voltage L1: " + str(etap.get_voltage(1)))
    print("Voltage L2: " + str(etap.get_voltage(2)))
    print("Voltage L3: " + str(etap.get_voltage(3)))
    # print("Current L1: " + str(etap.get_current(1)))
    # print("Current L2: " + str(etap.get_current(2)))
    # print("Current L3: " + str(etap.get_current(3)))
    # print("Board temperature: " + str(etap.get_board_temperature()))
    # print("EV plug temperature: " + str(etap.get_ev_plug_temperature()))
    # print("Grid plug temperature: " + str(etap.get_grid_plug_temperature()))
    print("Charger max. current: " + str(etap.get_max_current()))
    print("Charger mode: " + etap.get_mode())
    print("Charger mode int: " + str(etap.get_mode_int()))
    print("Setting current setpoint to 10A :" + str(etap.set_current_setpoint(10)))
    time.sleep(1)
    print("Charger max. current: " + str(etap.get_max_current()))
    #time.sleep(1)
    #print("Current setpoint: " + str(etap.get_current_setpoint()))
    etap.close()