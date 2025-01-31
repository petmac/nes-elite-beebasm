BEEBASM?=beebasm
PYTHON?=python

# A make command with no arguments will build the PAL variant with
# the standard commander and crc32 verification of the game binaries
#
# Optional arguments for the make command are:
#
#   variant=<release>   Build the specified variant:
#
#                         pal (default)
#                         ntsc
#
#   commander=max       Start with a maxed-out commander
#
#   match=no            Do not attempt to match the original game binaries
#                       (i.e. omit workspace noise)
#
#   verify=no           Disable crc32 verification of the game binaries
#
# So, for example:
#
#   make variant=ntsc commander=max match=no verify=no
#
# will build an NTSC variant with a maxed-out commander, no workspace noise
# and no crc32 verification

ifeq ($(commander), max)
  max-commander=TRUE
else
  max-commander=FALSE
endif

ifeq ($(encrypt), no)
  unencrypt=-u
  remove-checksums=TRUE
else
  unencrypt=
  remove-checksums=FALSE
endif

ifeq ($(match), no)
  match-original-binaries=FALSE
else
  match-original-binaries=TRUE
endif

ifeq ($(variant), ntsc)
  variant-number=1
  folder=/ntsc
  suffix=-ntsc
else
  variant-number=2
  folder=/pal
  suffix=-pal
endif

.PHONY:all
all:
	echo _VERSION=7 > 1-source-files/main-sources/elite-build-options.asm
	echo _VARIANT=$(variant-number) >> 1-source-files/main-sources/elite-build-options.asm
	echo _REMOVE_CHECKSUMS=$(remove-checksums) >> 1-source-files/main-sources/elite-build-options.asm
	echo _MATCH_ORIGINAL_BINARIES=$(match-original-binaries) >> 1-source-files/main-sources/elite-build-options.asm
	echo _MAX_COMMANDER=$(max-commander) >> 1-source-files/main-sources/elite-build-options.asm
	echo > 1-source-files/main-sources/elite-bank-options.asm
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-header.asm -v > 3-assembled-output/compile.txt
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-bank-0.asm -v > 3-assembled-output/compile0.txt
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-bank-1.asm -v > 3-assembled-output/compile1.txt
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-bank-2.asm -v > 3-assembled-output/compile2.txt
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-bank-3.asm -v > 3-assembled-output/compile3.txt
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-bank-4.asm -v > 3-assembled-output/compile4.txt
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-bank-5.asm -v > 3-assembled-output/compile5.txt
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-bank-6.asm -v > 3-assembled-output/compile6.txt
	echo _BANK=7 >> 1-source-files/main-sources/elite-bank-options.asm
	$(BEEBASM) -i 1-source-files/main-sources/elite-source-bank-7.asm -v > 3-assembled-output/compile7.txt
	cat 3-assembled-output/header.bin 3-assembled-output/bank0.bin 3-assembled-output/bank1.bin 3-assembled-output/bank2.bin 3-assembled-output/bank3.bin 3-assembled-output/bank4.bin 3-assembled-output/bank5.bin 3-assembled-output/bank6.bin 3-assembled-output/bank7.bin > 3-assembled-output/elite.bin
	cp 3-assembled-output/elite.bin 5-compiled-game-discs/ELITE$(suffix).NES
ifneq ($(verify), no)
	@$(PYTHON) 2-build-files/crc32.py 4-reference-binaries$(folder) 3-assembled-output
endif
