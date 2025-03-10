# modbus registers
## Charger modbus registers
### Station status registers
These registers are used to read statusses and apply overal settings to the charger. The modbus registers can be read at slave address 1.
| Register              | Start Address | Length | Type   | Read/Write | Description                 | Example           |  Implemented in version |
|-----------------------|---------------|--------|--------|------------|-----------------------------|-------------------|-------------------------|
| Name                  | 100           | 17     | STRING | READ       | Name of the device          | ETAP_34f928       | 0.1.0                   |
| Manufacturer          | 117           | 5      | STRING | READ       | Manufacturer of the device  | Some BV           | 0.1.0                   |
| Modbus table version  | 122           | 1      | INT16  | READ       | Modbus table version        | 3                 | 0.1.54                  |
| Firmware version      | 123           | 17     | STRING | READ       | Firmware version            | 0.1.54            | 0.1.54                  |
| reserved              | 140           | 17     | --     | --         | reserved                    |                   |                         |
| Serial number         | 157           | 11     | STRING | READ       | Serial number               | ETPRO11010000008  | 0.1.0                   |
| Datetime year         | 168           | 1      | INT16  | READ       | Datetime year               | 2024              | 0.1.0                   |
| Datetime month        | 169           | 1      | INT16  | READ       | Datetime month              | 1                 | 0.1.0                   |
| Datetime day          | 170           | 1      | INT16  | READ       | Datetime day                | 1                 | 0.1.0                   |
| Datetime hour         | 171           | 1      | INT16  | READ       | Datetime hour               | 0                 | 0.1.0                   |
| Datetime minute       | 172           | 1      | INT16  | READ       | Datetime minute             | 0                 | 0.1.0                   |
| Datetime second       | 173           | 1      | INT16  | READ       | Datetime second             | 0                 | 0.1.0                   |
| Uptime                | 174           | 4      | UINT64 | READ       | Uptime in seconds           | 123456            | 0.1.x                   |
| Time zone             | 178           | 1      | INT16  | READ       | Time zone to UTC (minutes)  | 0                 | 0.1.x                   |
| reserved              | 179           | 1      | --     | --         | reserved                    |                   |                         |
| NFC whitelist 1       | 180           | 5      | STRING | R/W        | NFC whitelist 1             | 12345678          | 0.1.x                   |
| NFC whitelist 2       | 195           | 5      | STRING | R/W        | NFC whitelist 2             | 12345678          | 0.1.x                   |
| NFC whitelist 3       | 190           | 5      | STRING | R/W        | NFC whitelist 3             | 12345678          | 0.1.x                   |
| NFC whitelist 4       | 195           | 5      | STRING | R/W        | NFC whitelist 4             | 12345678          | 0.1.x                   |
| NFC whitelist 5       | 200           | 5      | STRING | R/W        | NFC whitelist 5             | 12345678          | 0.1.x                   |
| NFC whitelist 6       | 205           | 5      | STRING | R/W        | NFC whitelist 6             | 12345678          | 0.1.x                   |
| NFC whitelist 7       | 210           | 5      | STRING | R/W        | NFC whitelist 7             | 12345678          | 0.1.x                   |
| NFC whitelist 8       | 215           | 5      | STRING | R/W        | NFC whitelist 8             | 12345678          | 0.1.x                   |


## Charger energy meter registers
These registers contain the energy metering data. The modbus registers can be read at slave address 1.
| Register              | Start Address | Length | Type   | Read/Write | Description                 | Example           |  Implemented in version |
|-----------------------|---------------|--------|--------|------------|-----------------------------|-------------------|-------------------------|
| Voltage L1-N          | 306           | 2      | FLOAT  | READ       | Voltage L1-N                | 230.0 V           | 0.1.0                   |
| Voltage L2-N          | 308           | 2      | FLOAT  | READ       | Voltage L2-N                | 230.0 V           | 0.1.0                   |
| Voltage L3-N          | 310           | 2      | FLOAT  | READ       | Voltage L3-N                | 230.0 V           | 0.1.0                   |
| reserved              | 312           | 8      | --     | --         | reserved                    |                   |                         |
| Current L1            | 320           | 2      | FLOAT  | READ       | Current L1                  | 16.0 A            | 0.1.54                  |
| Current L2            | 322           | 2      | FLOAT  | READ       | Current L2                  | 16.0 A            | 0.1.54                  |
| Current L3            | 324           | 2      | FLOAT  | READ       | Current L3                  | 16.0 A            | 0.1.54                  |
| Current sum           | 326           | 2      | FLOAT  | READ       | Sum of all current          | 16.0 A            | 0.1.54                  |
| reserved              | 328           | 10     | --     | --         | reserved                    |                   |                         |
| Active power L1       | 338           | 2      | FLOAT  | READ       | Active power L1             | 3680.0 W          | 0.1.54                  |
| Active power L2       | 340           | 2      | FLOAT  | READ       | Active power L2             | 3680.0 W          | 0.1.54                  |
| Active power L3       | 342           | 2      | FLOAT  | READ       | Active power L3             | 3680.0 W          | 0.1.54                  |
| Active power sum      | 344           | 2      | FLOAT  | READ       | Sum of all active power     | 11040.0 W         | 0.1.54                  |
| reserved              | 346           | 28     | --     | --         | reserved                    |                   |                         |
| Energy counter        | 374           | 4      | FLOAT  | READ       | Energy counter              | 12356.0 Wh        | 0.1.x                   |

## Charger status registers
These registers contain the current status of the charger. The modbus registers can be read at slave address 1.
| Register              | Start Address | Length | Type   | Read/Write | Description                 | Example           | Implemented in version  |
|-----------------------|---------------|--------|--------|------------|-----------------------------|-------------------|-------------------------|
| Charger max current   | 1100          | 2      | FLOAT  | READ       | Charger max current         | 16.0 A            | 0.1.0                   |
| Charger temperature   | 1102          | 2      | FLOAT  | READ       | Charger board temperature   | 25.0 degC         | 0.1.0                   |
| reserved              | 1104          | 2      | --     | --         | reserved                    |                   |                         |
| EV Plug temperature   | 1106          | 2      | FLOAT  | READ       | EV plug temperature         | 25.0 degC         | 0.1.0                   |
| Grid plug temperature | 1108          | 2      | FLOAT  | READ       | Grid plug temperature       | 25.0 degC         | 0.1.0                   |
| reserved              | 1110          | 20     | --     | --         | reserved                    |                   |                         |
| Availability          | 1200          | 1      | INT16  | READ       | Charger availability        | 1                 | 0.1.0                   |
| Mode                  | 1201          | 5      | STRING | READ       | Charger mode (status)       | C2                | 0.1.0                   |
| Applied max. current  | 1206          | 2      | STRING | FLOAT      | Applied setpoint            | 14.6 A            | 0.1.54                  |
| reserved              | 1208          | 2      | --     | --         | reserved                    |                   |                         |
| Current setpoint      | 1210          | 2      | FLOAT  | R/W        | Current setpoint            | 15.0 A            | 0.1.0                   |
| reserved              | 1212          | 2      | --     | --         | reserved                    |                   |                         |
| Setpoint status       | 1214          | 1      | UINT16 | READ       | Setpoint 1210 accounted for | 1                 | 0.1.54                  |
| Charging phases       | 1215          | 1      | UINT16 | R/W        | Number of charging phases   | 3                 | 0.1.54                  |
| reserved              | 1216          | 20     | --     | --         | reserved                    |                   |                         |
| Charge started by     | 1236          | 5      | STRING | READ       | Charge started by           | RFID              | 0.1.x                   |
| Session NFC           | 1241          | 5      | STRING | READ       | NFC UID for current session | 12345678          | 0.1.54                  |
| reserved              | 1246          | 1      | --     | ---        | reserved                    |                   |                         |
| GPS location          | 1247          | 17     | STRING | READ       | LON+LAT from NEMA GGA lock  |                   | 0.1.x                   |
