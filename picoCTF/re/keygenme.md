# Soluce

We got a keygenme binary, I expected to disas it but...
Look at the generated Ghidra C source code:


```C

undefined8 FUN_00101209(char *param_1)

{
  size_t sVar1;
  undefined8 uVar2;
  long in_FS_OFFSET;
  int local_d0;
  int local_cc;
  int local_c8;
  int local_c4;
  int local_c0;
  undefined2 local_ba;
  byte local_b8 [16];
  byte local_a8 [16];
  undefined8 local_98;
  undefined8 local_90;
  undefined8 local_88;
  undefined4 local_80;
  char local_78 [14];
  undefined local_6a;
  undefined local_62;
  undefined local_60;
  undefined local_5e;
  char local_58 [31];
  undefined local_39;
  char acStack56 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_98 = 0x7b4654436f636970; //picoCTF{
  local_90 = 0x30795f676e317262;
  local_88 = 0x6b5f6e77305f7275;
  local_80 = 0x5f7933;
  local_ba = 0x7d; // }
  
  
   ///// HASH
  sVar1 = strlen((char *)&local_98);
  MD5((uchar *)&local_98,sVar1,local_b8);
  sVar1 = strlen((char *)&local_ba);
  MD5((uchar *)&local_ba,sVar1,local_a8);
  //// HASH
  
  
  local_d0 = 0;
  
  for (local_cc = 0; local_cc < 16; local_cc = local_cc + 1) {
    sprintf(local_78 + local_d0,"%02x",(uint)local_b8[local_cc]);
    local_d0 = local_d0 + 2;
  }
  
  local_d0 = 0;
  
  for (local_c8 = 0; local_c8 < 16; local_c8 = local_c8 + 1) {
    sprintf(local_58 + local_d0,"%02x",(uint)local_a8[local_c8]);
    local_d0 = local_d0 + 2;
  }
  
  // How ????

  for (local_c4 = 0; local_c4 < 27; local_c4 = local_c4 + 1) {
    acStack56[local_c4] = *(char *)((long)&local_98 + (long)local_c4); //this statement dont have any sense...
  }
  
  acStack56[27] = local_5e;
  acStack56[28] = local_78[0];
  acStack56[29] = local_62;
  acStack56[30] = local_60;
  acStack56[31] = local_60;
  acStack56[32] = local_62;
  acStack56[33] = local_39;
  acStack56[34] = local_6a;
  acStack56[35] = (undefined)local_ba;
  sVar1 = strlen(param_1);
  if (sVar1 == 36) {
    for (local_c0 = 0; local_c0 < 36; local_c0 = local_c0 + 1) {
      if (param_1[local_c0] != acStack56[local_c0]) {
        uVar2 = 0;
        goto LAB_00101475;
      }
    }
    uVar2 = 1;
  }
  else {
    uVar2 = 0;
  }
LAB_00101475:
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return uVar2;
}

```

`acStack56[local_c4] = *(char *)((long)&local_98 + (long)local_c4);` => Is impossible and dont have any sense

When I saw it, i started GDB and put a breakpoint on any MOV with our array acStack56.
Let me know if you have somes solutions without debugging 