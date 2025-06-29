import device
import probe
import logging
from register import *
log = logging.getLogger()

Alarm_Translate = [ 0, 2] # 0 = No Alarm, 2 = Alarm



class Samsung_Battery(device.ModbusDevice):
    vendor_id = 'ss'
    vendor_name = 'Samsung SDI'
    productid = 0xb007
    productname = 'Samsung Lithium Ion Battery'
    min_timeout = 1
    allowed_roles = None
    default_role = 'battery'
    default_instance = 288

    def device_init(self):
        self.info_regs = [
            Reg_u16(0x0001, '/HardwareVersion', access='input'),
            Reg_u16(0x0001, '/FirmwareVersion', access='input'),
            Reg_u16(0x0001, '/Serial', access='input'),
        ]
        self.read_info()
        log.info('ELPM482-00005 Battery detected.')


        self.data_regs = [
            Reg_u16( 0x0004, '/Soc',                 1, '%.0f %%',access='input'),
            Reg_u16( 0x0005, '/Soh',                 1, '%.0f %%',access='input'),
            Reg_u16( 0x0002, '/Dc/0/Voltage',      100, '%.2f V',access='input'),
            Reg_s16( 0x0003, '/Dc/0/Current',        1, '%.1f A',access='input'),


            #Battery Information Registers for DVCC (Distributed Voltage and Current Control)
            Reg_u16(0x000f, '/Info/MaxChargeCurrent', 10, '%.1f A', access='input'),
            Reg_u16( 0x0010, '/Info/MaxDischargeCurrent',      10, '%.1f A', access='input'),
            Reg_u16( 0x000e, '/Info/BatteryLowVoltage',       100, '%.2f V', access='input'),
            Reg_u16( 0x000d, '/Info/MaxChargeVoltage',        100, '%.2f V', access='input'),
            
            
            #Tray Information Registers. Venus GX does not recognise trays, so we will use CellID as TrayID 
            Reg_u16( 0x000a, '/System/NrOfBatteries',access='input'),
            Reg_u16( 0x000b, '/System/NrOfModulesOnline',access='input'),
            Reg_u16( 0x000c, '/System/NrOfModulesOffline',access='input'),
            Reg_u16( 0x0019, '/System/MinCellVoltage',      1000, '%.3f V',access='input'),
            Reg_u16( 0x0020, '/System/MinCellVoltageCellId',access='input'),
            Reg_u16( 0x0017, '/System/MaxCellVoltage',      1000, '%.3f V',access='input'),
            Reg_u16( 0x0018, '/System/MaxCellVoltageCellId',access='input'),
            Reg_u16( 0x001c, '/System/MaxCellTemperature',access='input'),
            Reg_u16( 0x001d, '/System/MaxCellTemperatureCellId',access='input'),
            Reg_u16( 0x001e, '/System/MinCellTemperature',access='input'),
            Reg_u16( 0x001f, '/System/MinCellTemperatureCellId',access='input'),

            #Battery Error Registers
            Reg_bit(0x0006, '/Alarms/HighVoltage', text=Alarm_Translate, access='input', bit=0),
            Reg_bit(0x0006, '/Alarms/LowVoltage', text=Alarm_Translate, access='input', bit=1),
            Reg_bit(0x0006, '/Alarms/HighTemperature', text=Alarm_Translate, access='input', bit=2),
            Reg_bit(0x0006, '/Alarms/LowTemperature', text=Alarm_Translate, access='input', bit=3),
            Reg_bit(0x0006, '/Alarms/HighChargeCurrent', text=Alarm_Translate, access='input', bit=4),
            Reg_bit(0x0006, '/Alarms/HighDischargeCurrent', text=Alarm_Translate, access='input', bit=5),
            Reg_bit(0x0006, '/Alarms/CellImbalance', text=Alarm_Translate, access='input', bit=7),


        ]

models = {
# We dont have a unique model number for the Samsung Battery, so we will use the firmware version to identify the model
    259:   {
	'model':    'ELPM482-00005',
	'handler':  Samsung_Battery,
    }
}

probe.add_handler(probe.ModelRegister(Reg_u16(0x0001, access='input'), models,
                                      methods=['rtu'],
                                      rates=[57600], units=[1]))


   
