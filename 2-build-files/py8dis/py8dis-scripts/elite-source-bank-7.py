from commands import *


load(0xC000, "slices/bank7_first.bin", "6502")

config.set_lower_case(False)

# Remove all extras
config.set_label_references(False)
config.set_show_autogenerated_labels(False)
config.set_show_all_labels(False)
config.set_inline_comment_column(46)
config.set_subroutine_header("*" * 78)
config.set_indent_string(" ")

entry(0xC000)
entry(0xC007)
entry(0xC00C)
entry(0xC0A8)
entry(0xC582)
entry(0xC6F4)
entry(0xCD34)
entry(0xCD62)
entry(0xCD6F)
entry(0xCE90)
entry(0xCE9E)
entry(0xCEA5)
byte(0xCED2, 2)
entry(0xCED5)
entry(0xCF2E)
entry(0xD15B)
entry(0xD164)
entry(0xD17F)
entry(0xD195)
entry(0xD1C8)
entry(0xD715)
entry(0xD8C5)
entry(0xD8E1)
entry(0xD908)
entry(0xD919)
entry(0xD933)
entry(0xD946)
entry(0xD951)
entry(0xD96F)
entry(0xD986)
entry(0xDBD8)
entry(0xDC0F)
entry(0xE04A)
entry(0xE0B4)
entry(0xE0B7)
entry(0xE0BA)
entry(0xE33E)
entry(0xE543)
entry(0xE596)
entry(0xE59F)

byte(0xE5AB, 0xE5B0 - 0xE5AB)
hexadecimal(0xE5AB, 0xE5B0 - 0xE5AB)

label(0xE5B0, "LE5B0_EN")
byte(0xE5B0, 0xE602 - 0xE5B0)
hexadecimal(0xE5B0, 0xE602 - 0xE5B0)

label(0xE602, "LE602_DE")
byte(0xE602, 0xE653 - 0xE602)
hexadecimal(0xE602, 0xE653 - 0xE602)

label(0xE653, "LE653_FR")
byte(0xE653, 0xE6A4 - 0xE653)
hexadecimal(0xE653, 0xE6A4 - 0xE653)

label(0xE6A4, "LE6A4_subm_E802")
byte(0xE6A4, 0xE801 - 0xE6A4)
hexadecimal(0xE6A4, 0xE801 - 0xE6A4)

byte(0xEB27, 0xEB67 - 0xEB27)
hexadecimal(0xEB27, 0xEB67 - 0xEB27)

entry(0xEB67)
entry(0xEB86)
entry(0xEBA9)
entry(0xEC8D)
entry(0xECA0)
entry(0xECAE)
entry(0xECE2)
entry(0xECF9)
entry(0xED24)
entry(0xED81)
entry(0xED8F)
entry(0xED9D)
entry(0xEDA5)
entry(0xEDB9)
entry(0xEDDC)
entry(0xEDEA)
entry(0xEDFF)
entry(0xEE0D)
entry(0xEE15)
entry(0xEE2A)
entry(0xEE3F)
entry(0xEE54)
entry(0xEE62)
entry(0xEE7D)
entry(0xEE8B)
entry(0xEEA7)
entry(0xEEB5)
entry(0xEEC3)
entry(0xEECB)
entry(0xEED3)
entry(0xEEE8)
entry(0xEEF6)
entry(0xEF04)
entry(0xEF12)
entry(0xEF20)
entry(0xEF35)
entry(0xEF43)
entry(0xEF51)
entry(0xEF6C)
entry(0xEF7A)
entry(0xEF88)
entry(0xEF96)
entry(0xEFA4)
entry(0xEFB2)
entry(0xEFC0)
entry(0xEFCE)
entry(0xEFDC)
entry(0xEFEA)
entry(0xEFF7)
entry(0xF005)
entry(0xF013)
entry(0xF021)
entry(0xF02F)
entry(0xF03D)
entry(0xF04B)
entry(0xF059)
entry(0xF074)
entry(0xF082)
entry(0xF090)
entry(0xF09D)
entry(0xF0B8)
entry(0xF0C6)
entry(0xF0DC)
entry(0xF0E1)
entry(0xF0FC)
entry(0xF10A)
entry(0xF126)
entry(0xF15C)
entry(0xF171)
entry(0xF186)
entry(0xF194)
entry(0xF1A2)
entry(0xF1BD)
entry(0xF1CB)
entry(0xF1D9)
entry(0xF1E6)
entry(0xF201)
entry(0xF21C)
entry(0xF237)
entry(0xF245)
entry(0xF25A)
entry(0xF26E)
entry(0xF280)
entry(0xF293)
entry(0xF2A8)
entry(0xF2BD)
entry(0xF2CE)
entry(0xF2DE)
entry(0xF338)
entry(0xF37B)
entry(0xF3BC)
entry(0xF42A)
entry(0xF454)
entry(0xF461)
entry(0xF46A)
entry(0xF4AC)
entry(0xF4C1)
entry(0xF52D)
entry(0xF5AF)
entry(0xF60C)
entry(0xF65A)
entry(0xF664)
entry(0xF6BA)
entry(0xF70C)
entry(0xF718)
entry(0xF766)
entry(0xF7AB)
entry(0xF7CE)
entry(0xF83C)
entry(0xF853)
entry(0xF8AE)
entry(0xF8D1)
entry(0xFA13)
entry(0xFA16)
entry(0xFA33)
entry(0xFA43)
entry(0xFA55)
entry(0xFA8C)
entry(0xFA91)
entry(0xFACB)
entry(0xFAF8)

byte(0xFBCB, 0xFC00 - 0xFBCB)
hexadecimal(0xFBCB, 0xFC00 - 0xFBCB)

byte(0xFC00, 0xFCE8 - 0xFC00)
hexadecimal(0xFC00, 0xFCE8 - 0xFC00)

byte(0xFCE8, 0xFFFA - 0xFCE8)
hexadecimal(0xFCE8, 0xFFFA - 0xFCE8)

label(0x811E, "PlayMusic")
label(0x81B6, "slvy2")
label(0x8A14, "MVS5")
label(0x9522, "DemoShips")
label(0x9620, "tnpr")
label(0xA070, "LL9")
label(0xA379, "BR1")
label(0xA2C3, "DIALS")
label(0xA8D9, "TT27_0")
label(0xAC25, "SUN")
label(0xB0EF, "DETOK")
label(0xB187, "DTS")
label(0xB1BE, "STARS")
label(0xB1CA, "MAS4")
label(0xB2C3, "subm_B2C3")
label(0xB8F9, "GetSystemImage2")
label(0xB93C, "SetSystemImage2")
label(0xB341, "ClearTiles")
label(0xB3E8, "PDESC")
label(0xB44F, "TT27")
label(0xB4AA, "ex")
label(0xB4F5, "DASC")
label(0xB635, "CHPR")
label(0xB738, "HALL")
label(0xB85C, "TIDY")
label(0xB8F7, "PAS1")
label(0xB975, "SCAN")
label(0xB980, "LL164")
label(0xBC83, "TITLE")
label(0xBEB5, "TT66")
label(0xBEEA, "GetSystemImage1")
label(0xBED7, "SetSystemImage1")

exec(open('py8dis-scripts/common-variables.py').read())

go()
