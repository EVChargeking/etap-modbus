# modbus registers
## Charger modbus registers
These registers are used to read statusses and apply overal settings to the charger. The modbus registers can be read at slave address 200.
| Register              | Start Address | Length | Type   | Read/Write | Description                 | Example           |
|-----------------------|---------------|--------|--------|------------|-----------------------------|-------------------|
| Name                  | 100           | 17     | STRING | READ       | Name of the device          | ETAP_34f928       |
| Manufacturer          | 117           | 5      | STRING | READ       | Manufacturer of the device  | Some BV           |
| Modbus table version  | 122           | 1      | INT16  | READ       | Modbus table version        | 1                 |
| Firmware version      | 123           | 17     | STRING | READ       | Firmware version            | 1.0.0             |
| reserved              | 140           | 17     | --     | --         | reserved                    |                   |
| Serial number         | 157           | 11     | STRING | READ       | Serial number               | ETPRO11010000008  |
| Datetime year         | 168           | 1      | INT16  | READ       | Datetime year               | 2024              |
| Datetime month        | 169           | 1      | INT16  | READ       | Datetime month              | 1                 |
| Datetime day          | 170           | 1      | INT16  | READ       | Datetime day                | 1                 |
| Datetime hour         | 171           | 1      | INT16  | READ       | Datetime hour               | 0                 |
| Datetime minute       | 172           | 1      | INT16  | READ       | Datetime minute             | 0                 |
| Datetime second       | 173           | 1      | INT16  | READ       | Datetime second             | 0                 |
| Uptime                | 174           | 4      | UINT64 | READ       | Uptime in seconds           | 123456            |
| Time zone             | 178           | 1      | INT16  | READ       | Time zone to UTC (minutes)  | 0                 |
| Charger max current   | 1100          | 2      | FLOAT  | READ       | Charger max current         | 16.0 A            |
| Charger temperature   | 1102          | 2      | FLOAT  | READ       | Charger board temperature   | 25.0 degC         |
| reserved              | 1104          | 2      | --     | --         | reserved                    |                   |
| EV Plug temperature   | 1106          | 2      | FLOAT  | READ       | EV plug temperature         | 25.0 degC         |
| Grid plug temperature | 1108          | 2      | FLOAT  | READ       | Grid plug temperature       | 25.0 degC         |
| reserved              | 1110          | 20     | --     | --         | reserved                    |                   |
| NFC whitelist 1       | 1130          | 5      | STRING | R/W        | NFC whitelist 1             | 12345678          |
| NFC whitelist 2       | 1135          | 5      | STRING | R/W        | NFC whitelist 2             | 12345678          |
| NFC whitelist 3       | 1140          | 5      | STRING | R/W        | NFC whitelist 3             | 12345678          |
| NFC whitelist 4       | 1145          | 5      | STRING | R/W        | NFC whitelist 4             | 12345678          |
| NFC whitelist 5       | 1150          | 5      | STRING | R/W        | NFC whitelist 5             | 12345678          |
| NFC whitelist 6       | 1155          | 5      | STRING | R/W        | NFC whitelist 6             | 12345678          |
| NFC whitelist 7       | 1160          | 5      | STRING | R/W        | NFC whitelist 7             | 12345678          |
| NFC whitelist 8       | 1165          | 5      | STRING | R/W        | NFC whitelist 8             | 12345678          |

## Charger energy meter registers
These registers contain the energy metering data. The modbus registers can be read at slave address 1.
| Register              | Start Address | Length | Type   | Read/Write | Description                 | Example           |
|-----------------------|---------------|--------|--------|------------|-----------------------------|-------------------|
| Voltage L1-N          | 306           | 2      | FLOAT  | READ       | Voltage L1-N                | 230.0 V           |
| Voltage L2-N          | 308           | 2      | FLOAT  | READ       | Voltage L2-N                | 230.0 V           |
| Voltage L3-N          | 310           | 2      | FLOAT  | READ       | Voltage L3-N                | 230.0 V           |
| reserved              | 312           | 8      | --     | --         | reserved                    |                   |
| Current L1            | 320           | 2      | FLOAT  | READ       | Current L1                  | 16.0 A            |
| Current L2            | 322           | 2      | FLOAT  | READ       | Current L2                  | 16.0 A            |
| Current L3            | 324           | 2      | FLOAT  | READ       | Current L3                  | 16.0 A            |
| Current sum           | 326           | 2      | FLOAT  | READ       | Sum of all current          | 16.0 A            |
| Reserved              | 328           | 10     | --     | --         | reserved                    |                   |
| Active power L1       | 338           | 2      | FLOAT  | READ       | Active power L1             | 3680.0 W          |
| Active power L2       | 340           | 2      | FLOAT  | READ       | Active power L2             | 3680.0 W          |
| Active power L3       | 342           | 2      | FLOAT  | READ       | Active power L3             | 3680.0 W          |
| Active power sum      | 344           | 2      | FLOAT  | READ       | Sum of all active power     | 11040.0 W         |
| Reserved              | 346           | 28     | --     | --         | reserved                    |                   |
| Energy counter        | 374           | 4      | FLOAT  | READ       | Energy counter              | 12356.0 Wh        |

## Charger status registers
These registers contain the current status of the charger. The modbus registers can be read at slave address 1.
| Register              | Start Address | Length | Type   | Read/Write | Description                 | Example           |
|-----------------------|---------------|--------|--------|------------|-----------------------------|-------------------|
| Availability          | 1200          | 1      | INT16  | READ       | Charger availability        | 1                 |
| Mode                  | 1201          | 5      | STRING | READ       | Charger mode (status)       | C2                |
| Applied max. current  | 1206          | 2      | STRING | FLOAT      | Applied setpoint            | 14.6 A            |
| reserved              | 1208          | 2      | --     | --         | reserved                    |                   |
| Current setpoint      | 1210          | 2      | FLOAT  | R/W        | Current setpoint            | 15.0 A            |
| reserved              | 1212          | 2      | --     | --         | reserved                    |                   |
| Setpoint status       | 1214          | 1      | UINT16 | READ       | Setpoint deviation reason   | 1                 |
| Charging phases       | 1215          | 1      | UINT16 | R/W        | Number of charging phases   | 3                 |
| reserved              | 1216          | 20     | --     | --         | reserved                    |                   |
| charge started by     | 1236          | 5      | STRING | READ       | Charge started by           | RFID              |
| session NFC           | 1241          | 5      | STRING | READ       | NFC UID for current session | 12345678          |





