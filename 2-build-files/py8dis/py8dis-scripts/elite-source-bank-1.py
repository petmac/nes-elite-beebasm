from commands import *


load(0x8000, "slices/bank1.bin", "6502")

config.set_lower_case(False)

# Remove all extras
config.set_label_references(False)
config.set_show_autogenerated_labels(False)
config.set_show_all_labels(False)
config.set_inline_comment_column(50)
config.set_subroutine_header("*" * 78)

entry(0x8000)
string(0x8007, 5)

word(0x800C, 1)
word(0x800E, 1)
word(0x8010, 1)
word(0x8012, 1)
word(0x8014, 1)
word(0x8016, 1)
word(0x8018, 1)
word(0x801A, 1)
word(0x801C, 1)
word(0x801E, 1)
word(0x8020, 1)
word(0x8022, 1)
word(0x8024, 1)
word(0x8026, 1)
word(0x8028, 1)
word(0x802A, 1)
word(0x802C, 1)
word(0x802E, 1)
word(0x8030, 1)
word(0x8032, 1)
word(0x8034, 1)
word(0x8036, 1)
word(0x8038, 1)
word(0x803A, 1)
word(0x803C, 1)
word(0x803E, 1)
word(0x8040, 1)

#byte(0xB575, 4)

entry(0xA06D)
entry(0xA070)
entry(0xA3F0)
entry(0xA6A0)
entry(0xA8F2)
entry(0xAA54)
entry(0xAA55)
entry(0xB1BE)
entry(0xB79E)
entry(0xB738)
entry(0xB75F)
entry(0xB77C)
entry(0xB7A5)
entry(0xB7D4)
entry(0xB969)
entry(0xB975)
entry(0xBAE2)

label(0x800C, "XX21_NOISE")
label(0x8042, "E_per_cent")
label(0x8063, "KWL_per_cent")
label(0x8084, "KWH_per_cent")
label(0x80A5, "SHIP_MISSILE")
label(0x81A3, "SHIP_CORIOLIS")
label(0x82BF, "SHIP_ESCAPE_POD")
label(0x8313, "SHIP_PLATE")
label(0x8353, "SHIP_CANISTER")
label(0x83FB, "SHIP_BOULDER")
label(0x849D, "SHIP_ASTEROID")
label(0x8573, "SHIP_SPLINTER")
label(0x85AF, "SHIP_SHUTTLE")
label(0x86E1, "SHIP_TRANSPORTER")
label(0x88C3, "SHIP_COBRA_MK_3")
label(0x8A4B, "SHIP_PYTHON")
label(0x8B3D, "SHIP_BOA")
label(0x8C33, "SHIP_ANACONDA")
label(0x8D35, "SHIP_ROCK_HERMIT") # bigger than in Master
label(0x8E0B, "SHIP_VIPER")
label(0x8EE5, "SHIP_SIDEWINDER")
label(0x8F8D, "SHIP_MAMBA")
label(0x90BB, "SHIP_KRAIT")
label(0x91A1, "SHIP_ADDER")
label(0x92D1, "SHIP_GECKO")
label(0x9395, "SHIP_COBRA_MK_1")
label(0x945B, "SHIP_WORM")
label(0x950B, "SHIP_COBRA_MK_3_P")
label(0x9693, "SHIP_ASP_MK_2")
label(0x97BD, "SHIP_PYTHON_P")
label(0x98AF, "SHIP_FER_DE_LANCE")
label(0x99C9, "SHIP_MORAY")
label(0x9AA1, "SHIP_THARGOID")
label(0x9BBD, "SHIP_THARGON")
label(0x9C29, "SHIP_CONSTRICTOR")
label(0x9D2B, "SHIP_COUGAR")
label(0x9E2D, "SHIP_DODO")
label(0x9F89, "4bytesofnoise")
label(0x9FC6, "Shpt")

label(0xA0CE, "EE28")
label(0xA0D2, "LL14")
label(0xA201, "LL86")
label(0xA25F, "ovflw")
label(0xA32D, "LL88")
label(0xA37B, "LL48")
label(0xA3D4, "LL49")
label(0xA3F9, "LL52")
label(0xA41C, "LL53")
label(0xA459, "LL55")
label(0xA529, "LL70")
label(0xA556, "LL50")
label(0xA57A, "EE1")
label(0xA620, "LL79")
label(0xAA88, "PL20")
label(0xAC15, "PLF3")
label(0xAF7A, "RTS2")
label(0xAFFB, "ED3")
label(0xB003, "ED1")
label(0xB15C, "BL1")
label(0xB2D0, "KILL1")
label(0xB545, "KILL2")
label(0xB714, "HATB")
label(0xB840, "TI2")

subroutine(0x9F8D, "SHPPT")
subroutine(0x9FDC, "LL38")
subroutine(0x9FFC, "LL51")
subroutine(0xA06D, "LL25")
subroutine(0xA070, "LL9")
subroutine(0xA0E8, "LL10")
subroutine(0xA13C, "LL17")
subroutine(0xA19A, "EE29")
subroutine(0xA334, "LL42")
subroutine(0xA41C, "LL53")
subroutine(0xA46D, "LL61")
subroutine(0xA494, "LL62")
subroutine(0xA4A7, "LL56")
subroutine(0xA4C6, "LL57")
subroutine(0xA4DD, "LL60")
subroutine(0xA513, "LL66")
subroutine(0xA56B, "LL72")
subroutine(0xA5D9, "LL170")
subroutine(0xA5F2, "LL75")
subroutine(0xA65D, "CLIP")
subroutine(0xA664, "CLIP2")
subroutine(0xA7B0, "LL78")
subroutine(0xA7CA, "LL118")
subroutine(0xA8FD, "DOEXP")
subroutine(0xAA21, "EXS1")
subroutine(0xAA54, "PL2")
subroutine(0xAA55, "PLANET")
subroutine(0xAA7F, "PL9")
subroutine(0xAA8F, "PL9_2")
subroutine(0xAACD, "PL26")
subroutine(0xAACD, "PL26")
subroutine(0xAB27, "PLS1")
subroutine(0xAB45, "PLS2")
subroutine(0xAB49, "PLS22")
subroutine(0xAC25, "SUN")
subroutine(0xAF7B, "CIRCLE")
subroutine(0xAF9D, "CIRCLE2")
subroutine(0xB014, "EDGES")
subroutine(0xB077, "CHKON")
subroutine(0xB0AF, "PL21")
subroutine(0xB0B3, "PLS3")
subroutine(0xB0D4, "PLS4")
subroutine(0xB0E4, "PLS5")
subroutine(0xB0F5, "ARCTAN")
subroutine(0xB13B, "BLINE")
subroutine(0xB1BE, "STARS")
subroutine(0xB1CC, "STARS1")
subroutine(0xB302, "STARS6")
subroutine(0xB43F, "STARS2")
subroutine(0xB738, "HALL")
subroutine(0xB7A5, "ZINF")
subroutine(0xB7D4, "HAS1")
subroutine(0xB85C, "TIDY")
subroutine(0xB923, "TIS3")
subroutine(0xB942, "DVIDT")
subroutine(0xBBFA, "PIXEL2")

exec(open('py8dis-scripts/common-variables.py').read())

go()
