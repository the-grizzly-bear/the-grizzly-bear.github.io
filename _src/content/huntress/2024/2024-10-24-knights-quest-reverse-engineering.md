# 2024-10-24 Knight's Quest (Reverse Engineering)

*[image unavailable]*

Interesting program, fight a spider, and ogre, then Gorthmog
*[image unavailable]*

*[image unavailable]*

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

```python

void knightsquest/game.(*Game).runGameLoop(void)

{
  byte bVar1;
  char cVar2;
  undefined8 *in_RAX;
  undefined8 *puVar3;
  long lVar4;
  long lVar5;
  undefined8 extraout_RDX;
  byte bVar6;
  long unaff_R14;
  undefined in_XMM15 [16];
  undefined auVar7 [16];
  undefined8 *puStack0000000000000008;
  undefined local_2f8 [40];
  undefined local_2d0 [40];
  undefined local_2a8 [40];
  undefined local_280 [48];
  undefined8 local_250;
  undefined8 local_248;
  undefined8 local_240;
  undefined8 local_238;
  undefined8 local_230;
  undefined8 local_228;
  undefined8 local_220;
  undefined8 local_218;
  undefined8 local_210;
  undefined8 local_208;
  long local_200;
  undefined8 local_1f8;
  undefined8 local_1f0;
  undefined local_1e8 [56];
  undefined local_1b0 [24];
  code *local_198;
  undefined8 local_190;
  undefined local_188 [88];
  undefined *local_130;
  undefined **local_128;
  code *local_120;
  undefined8 local_118;
  code *local_110;
  undefined8 local_108;
  undefined local_100 [16];
  undefined8 local_f0;
  undefined8 *local_e8;
  undefined8 *local_e0;
  undefined local_d8 [16];
  undefined8 local_c8;
  undefined **local_c0;
  undefined8 local_b8;
  undefined local_a8 [24];
  undefined8 local_90;
  undefined8 local_88;
  undefined local_80 [88];
  undefined *local_28;
  undefined **local_20;
  undefined local_18 [16];

  puStack0000000000000008 = in_RAX;
  while (local_280 <= *(undefined **)(unaff_R14 + 0x10)) {
    runtime.morestack_noctxt();
  }
  puVar3 = (undefined8 *)puStack0000000000000008[0xb];
  lVar5 = puStack0000000000000008[0xc];
  while( true ) {
    local_80._8_8_ = in_XMM15._8_8_;
    if (lVar5 < 1) {
      local_d8._0_8_ = *puStack0000000000000008;
      local_e8 = puStack0000000000000008 + 1;
      FUN_0046ca7a(local_d8 + 8);
      FUN_0046ca7a(local_2f8,local_d8 + 8);
      FUN_0046c710(local_2d0);
      knightsquest/renderer.RenderScreen();
      local_208 = 0x20;
      local_190 = github.com/fatih/color.New();
      local_198 = knightsquest/game.(*Game).runGameLoop.(*Color).SprintFunc.func3;
      knightsquest/renderer.AddMessage();
      local_d8._0_8_ = *puStack0000000000000008;
      FUN_0046ca7a(local_d8 + 8,local_e8);
      FUN_0046ca7a(local_2f8,local_d8 + 8);
      FUN_0046c710(local_2d0);
      knightsquest/renderer.RenderScreen();
      local_250 = 0x446b684155444f42;
      local_248 = 0x63374d5a336a4c4d;
      local_240 = 0x31746c4255396f66;
      local_238 = 0x6e4c375942554e41;
      local_230 = 0x384c686770646365;
      local_228 = 0x6236734a595a676d;
      local_220 = 0x657a514d666e6f68;
      local_218 = 0x514c344970736a44;
      lVar5 = runtime.makeslice();
      for (lVar4 = 0; lVar4 < 0x20; lVar4 = lVar4 + 1) {
        bVar1 = (*(byte *)((long)&local_250 + lVar4) ^ *(byte *)((long)&local_230 + lVar4)) % 0x3e;
        bVar6 = bVar1 + 0x41;
        *(byte *)(lVar5 + lVar4) = bVar6;
        if (0x5a < bVar6) {
          if (bVar6 < 0x61) {
            *(byte *)(lVar5 + lVar4) = bVar1 + 0x47;
          }
          else if (0x7a < bVar6) {
            *(byte *)(lVar5 + lVar4) = bVar1 - 10;
          }
        }
      }
      runtime.slicebytetostring();
      local_18._8_8_ = runtime.convTstring();
      local_18._0_8_ = &DAT_004a2ce0;
      fmt.Fprintf(0x25,local_18,&DAT_004a2ce0,&DAT_004c062f,1,1);
      local_28 = &DAT_004a2ce0;
      local_20 = &PTR_s_Press_enter_to_exit_the_game..._004e0e68;
      fmt.Fprintln(1,1,&PTR_s_Press_enter_to_exit_the_game..._004e0e68,&local_28);
      local_f0 = DAT_00568300;
      FUN_0046c710(local_a8);
      runtime.makeslice();
      local_d8._0_8_ = FUN_0046c710(local_100);
      local_d8._8_8_ = 0x1000;
      local_c8 = 0x1000;
      local_c0 = &PTR_DAT_004e1468;
      local_b8 = local_f0;
      local_90 = 0xffffffffffffffff;
      local_88 = 0xffffffffffffffff;
      local_80._0_8_ = local_d8._0_8_;
      FUN_0046ca7a(local_80 + 8,local_d8 + 8);
      bufio.(*Reader).ReadString();
      return;
    }
    local_d8._0_8_ = *puVar3;
    local_200 = lVar5;
    local_e0 = puVar3;
    FUN_0046ca7a(local_d8 + 8,puVar3 + 1);
    local_1f0 = local_d8._0_8_;
    FUN_0046ca7a(local_1e8,local_d8 + 8);
    auVar7 = runtime.convTstring();
    local_100._8_8_ = auVar7._0_8_;
    local_100._0_8_ = &DAT_004a2ce0;
    local_1f8 = fmt.Sprintf(1,1,auVar7._8_8_,local_100);
    local_210 = 0x12;
    local_208 = 0x1f;
    local_108 = github.com/fatih/color.New();
    local_110 = knightsquest/game.(*Game).runGameLoop.(*Color).SprintFunc.func1;
    knightsquest/renderer.AddMessage();
    cVar2 = knightsquest/round.PlayRound();
    local_188._8_8_ = in_XMM15._8_8_;
    if (cVar2 == '\0') break;
    puVar3 = local_e0 + 0xb;
    lVar5 = local_200 + -1;
  }
  local_e8 = puStack0000000000000008 + 1;
  local_d8._0_8_ = *puStack0000000000000008;
  FUN_0046ca7a(local_d8 + 8,local_e8);
  FUN_0046ca7a(local_2f8,local_d8 + 8);
  local_2a8._0_8_ = local_1f0;
  FUN_0046ca7a(local_2a8 + 8,local_1e8);
  knightsquest/renderer.RenderScreen();
  local_208 = 0x1f;
  local_118 = github.com/fatih/color.New();
  local_120 = knightsquest/game.(*Game).runGameLoop.(*Color).SprintFunc.func2;
  knightsquest/renderer.AddMessage();
  local_d8._0_8_ = *puStack0000000000000008;
  FUN_0046ca7a(local_d8 + 8,local_e8);
  FUN_0046ca7a(local_2f8,local_d8 + 8);
  local_2a8._0_8_ = local_1f0;
  FUN_0046ca7a(local_2a8 + 8,local_1e8);
  knightsquest/renderer.RenderScreen();
  local_130 = &DAT_004a2ce0;
  local_128 = &PTR_s_Press_enter_to_exit_the_game..._004e0e68;
  fmt.Fprintln(1,1,extraout_RDX,&local_130);
  local_f0 = DAT_00568300;
  FUN_0046c710(local_1b0);
  runtime.makeslice();
  local_d8._0_8_ = FUN_0046c710(local_100);
  local_d8._8_8_ = 0x1000;
  local_c8 = 0x1000;
  local_c0 = &PTR_DAT_004e1468;
  local_b8 = local_f0;
  local_90 = 0xffffffffffffffff;
  local_88 = 0xffffffffffffffff;
  local_188._0_8_ = local_d8._0_8_;
  FUN_0046ca7a(local_188 + 8,local_d8 + 8);
  bufio.(*Reader).ReadString();
  return;
}

```

Other functions extracted
```python
undefined8 knightsquest/round.playerTurn(void)

{
  undefined8 *in_RAX;
  int *piVar1;
  undefined8 uVar2;
  undefined8 *extraout_RDX;
  undefined8 *extraout_RDX_00;
  undefined8 *unaff_RBX;
  undefined8 *in_R11;
  long unaff_R14;
  undefined auVar3 [16];
  undefined8 *param_7;
  undefined8 *param_8;
  undefined local_1f0 [80];
  undefined8 local_1a0;
  undefined local_198 [32];
  undefined local_178 [48];
  long local_148;
  undefined8 local_140;
  undefined8 local_138;
  undefined8 local_130;
  code *local_128;
  undefined8 local_120;
  code *local_118;
  undefined8 local_110;
  code *local_108;
  undefined8 local_100;
  code *local_f8;
  undefined8 local_f0;
  undefined8 local_e8;
  undefined local_e0 [80];
  undefined8 local_90;
  undefined local_88 [80];
  undefined local_38 [16];
  undefined local_28 [16];
  undefined local_18 [16];

  param_7 = in_RAX;
  while (param_8 = unaff_RBX, local_178 <= *(undefined **)(unaff_R14 + 0x10)) {
    runtime.morestack_noctxt();
    unaff_RBX = param_8;
  }
  local_90 = *param_7;
  FUN_0046ca7a(local_88,param_7 + 1);
  local_e8 = *unaff_RBX;
  FUN_0046ca7a(local_e0,unaff_RBX + 1);
  FUN_0046ca7a(local_1f0,local_88);
  local_1a0 = local_e8;
  FUN_0046ca7a(local_198,local_e0);
  knightsquest/renderer.RenderScreen();
  piVar1 = (int *)knightsquest/prompt.GetPlayerAction();
  if (unaff_RBX == (undefined8 *)0x6) {
    if ((*piVar1 == 0x61747461) && (*(short *)(piVar1 + 1) == 0x6b63)) {
      if (*(char *)(param_8 + 8) == '\0') {
        local_148 = param_7[4];
        param_8[3] = param_8[3] - local_148;
        local_38._8_8_ = runtime.convTstring();
        local_38._0_8_ = &DAT_004a2ce0;
        auVar3 = runtime.convT64();
        local_28._8_8_ = auVar3._0_8_;
        local_28._0_8_ = &DAT_004a2f20;
        local_130 = fmt.Sprintf(2,2,auVar3._8_8_,local_38);
        local_140 = 0x22;
        local_138 = 0x20;
        local_100 = github.com/fatih/color.New();
        local_108 = knightsquest/round.playerTurn.(*Color).SprintFunc.func2;
        knightsquest/renderer.AddMessage();
      }
      else {
        auVar3 = runtime.convTstring();
        local_18._8_8_ = auVar3._0_8_;
        local_18._0_8_ = &DAT_004a2ce0;
        local_130 = fmt.Sprintf(1,1,auVar3._8_8_,local_18);
        local_140 = 0x1b;
        local_138 = 0x20;
        local_f0 = github.com/fatih/color.New();
        local_f8 = knightsquest/round.playerTurn.(*Color).SprintFunc.func1;
        knightsquest/renderer.AddMessage();
        *(undefined *)(param_8 + 8) = 0;
      }
      param_7[7] = 6;
      if (DAT_005884a0 != 0) {
        uVar2 = param_7[6];
        runtime.gcWriteBarrier1();
        *in_R11 = uVar2;
        param_7 = extraout_RDX;
      }
      param_7[6] = &DAT_004ba258;
    }
    else if ((*piVar1 == 0x65666564) && (*(short *)(piVar1 + 1) == 0x646e)) {
      *(undefined *)(param_7 + 8) = 1;
      local_138 = 0x20;
      local_110 = github.com/fatih/color.New();
      local_118 = knightsquest/round.playerTurn.(*Color).SprintFunc.func3;
      knightsquest/renderer.AddMessage();
      param_7[7] = 6;
      if (DAT_005884a0 != 0) {
        uVar2 = param_7[6];
        runtime.gcWriteBarrier1();
        *in_R11 = uVar2;
        param_7 = extraout_RDX_00;
      }
      param_7[6] = &DAT_004ba25e;
    }
  }
  if (0 < (long)param_8[3]) {
    return 0;
  }
  auVar3 = runtime.convTstring();
  local_18._8_8_ = auVar3._0_8_;
  local_18._0_8_ = &DAT_004a2ce0;
  local_130 = fmt.Sprintf(1,1,auVar3._8_8_,local_18);
  local_140 = 0x19;
  local_138 = 0x20;
  local_120 = github.com/fatih/color.New();
  local_128 = knightsquest/round.playerTurn.(*Color).SprintFunc.func4;
  knightsquest/renderer.AddMessage();
  return 1;
}

undefined8 knightsquest/round.playerTurn(void)

{
  undefined8 *in_RAX;
  int *piVar1;
  undefined8 uVar2;
  undefined8 *extraout_RDX;
  undefined8 *extraout_RDX_00;
  undefined8 *unaff_RBX;
  undefined8 *in_R11;
  long unaff_R14;
  undefined auVar3 [16];
  undefined8 *param_7;
  undefined8 *param_8;
  undefined local_1f0 [80];
  undefined8 local_1a0;
  undefined local_198 [32];
  undefined local_178 [48];
  long local_148;
  undefined8 local_140;
  undefined8 local_138;
  undefined8 local_130;
  code *local_128;
  undefined8 local_120;
  code *local_118;
  undefined8 local_110;
  code *local_108;
  undefined8 local_100;
  code *local_f8;
  undefined8 local_f0;
  undefined8 local_e8;
  undefined local_e0 [80];
  undefined8 local_90;
  undefined local_88 [80];
  undefined local_38 [16];
  undefined local_28 [16];
  undefined local_18 [16];

  param_7 = in_RAX;
  while (param_8 = unaff_RBX, local_178 <= *(undefined **)(unaff_R14 + 0x10)) {
    runtime.morestack_noctxt();
    unaff_RBX = param_8;
  }
  local_90 = *param_7;
  FUN_0046ca7a(local_88,param_7 + 1);
  local_e8 = *unaff_RBX;
  FUN_0046ca7a(local_e0,unaff_RBX + 1);
  FUN_0046ca7a(local_1f0,local_88);
  local_1a0 = local_e8;
  FUN_0046ca7a(local_198,local_e0);
  knightsquest/renderer.RenderScreen();
  piVar1 = (int *)knightsquest/prompt.GetPlayerAction();
  if (unaff_RBX == (undefined8 *)0x6) {
    if ((*piVar1 == 0x61747461) && (*(short *)(piVar1 + 1) == 0x6b63)) {
      if (*(char *)(param_8 + 8) == '\0') {
        local_148 = param_7[4];
        param_8[3] = param_8[3] - local_148;
        local_38._8_8_ = runtime.convTstring();
        local_38._0_8_ = &DAT_004a2ce0;
        auVar3 = runtime.convT64();
        local_28._8_8_ = auVar3._0_8_;
        local_28._0_8_ = &DAT_004a2f20;
        local_130 = fmt.Sprintf(2,2,auVar3._8_8_,local_38);
        local_140 = 0x22;
        local_138 = 0x20;
        local_100 = github.com/fatih/color.New();
        local_108 = knightsquest/round.playerTurn.(*Color).SprintFunc.func2;
        knightsquest/renderer.AddMessage();
      }
      else {
        auVar3 = runtime.convTstring();
        local_18._8_8_ = auVar3._0_8_;
        local_18._0_8_ = &DAT_004a2ce0;
        local_130 = fmt.Sprintf(1,1,auVar3._8_8_,local_18);
        local_140 = 0x1b;
        local_138 = 0x20;
        local_f0 = github.com/fatih/color.New();
        local_f8 = knightsquest/round.playerTurn.(*Color).SprintFunc.func1;
        knightsquest/renderer.AddMessage();
        *(undefined *)(param_8 + 8) = 0;
      }
      param_7[7] = 6;
      if (DAT_005884a0 != 0) {
        uVar2 = param_7[6];
        runtime.gcWriteBarrier1();
        *in_R11 = uVar2;
        param_7 = extraout_RDX;
      }
      param_7[6] = &DAT_004ba258;
    }
    else if ((*piVar1 == 0x65666564) && (*(short *)(piVar1 + 1) == 0x646e)) {
      *(undefined *)(param_7 + 8) = 1;
      local_138 = 0x20;
      local_110 = github.com/fatih/color.New();
      local_118 = knightsquest/round.playerTurn.(*Color).SprintFunc.func3;
      knightsquest/renderer.AddMessage();
      param_7[7] = 6;
      if (DAT_005884a0 != 0) {
        uVar2 = param_7[6];
        runtime.gcWriteBarrier1();
        *in_R11 = uVar2;
        param_7 = extraout_RDX_00;
      }
      param_7[6] = &DAT_004ba25e;
    }
  }
  if (0 < (long)param_8[3]) {
    return 0;
  }
  auVar3 = runtime.convTstring();
  local_18._8_8_ = auVar3._0_8_;
  local_18._0_8_ = &DAT_004a2ce0;
  local_130 = fmt.Sprintf(1,1,auVar3._8_8_,local_18);
  local_140 = 0x19;
  local_138 = 0x20;
  local_120 = github.com/fatih/color.New();
  local_128 = knightsquest/round.playerTurn.(*Color).SprintFunc.func4;
  knightsquest/renderer.AddMessage();
  return 1;
}
/* WARNING: Removing unreachable block (ram,0x00498575) */
/* WARNING: Removing unreachable block (ram,0x0049857d) */

undefined8 knightsquest/round.enemyTurn(void)

{
  long in_RAX;
  long extraout_RDX;
  long unaff_RBX;
  undefined8 uVar1;
  undefined8 *in_R11;
  long unaff_R14;
  undefined auVar2 [16];
  long param_7;
  long param_8;
  undefined8 local_40;
  undefined local_38 [16];
  undefined local_28 [16];
  undefined local_18 [16];

  param_7 = in_RAX;
  param_8 = unaff_RBX;
  while (&local_40 <= *(undefined8 **)(unaff_R14 + 0x10)) {
    runtime.morestack_noctxt();
  }
  auVar2 = runtime.convTstring();
  local_18._8_8_ = auVar2._0_8_;
  local_18._0_8_ = &DAT_004a2ce0;
  fmt.Sprintf(1,1,auVar2._8_8_,local_18);
  local_40 = github.com/fatih/color.New();
  knightsquest/renderer.AddMessage();
  if (*(char *)(param_7 + 0x40) == '\0') {
    *(long *)(param_7 + 0x18) = *(long *)(param_7 + 0x18) - *(long *)(param_8 + 0x20);
    local_38._8_8_ = runtime.convTstring();
    local_38._0_8_ = &DAT_004a2ce0;
    auVar2 = runtime.convT64();
    local_28._8_8_ = auVar2._0_8_;
    local_28._0_8_ = &DAT_004a2f20;
    fmt.Sprintf(2,2,auVar2._8_8_,local_38);
    github.com/fatih/color.New();
    knightsquest/renderer.AddMessage();
  }
  else {
    auVar2 = runtime.convTstring();
    local_18._8_8_ = auVar2._0_8_;
    local_18._0_8_ = &DAT_004a2ce0;
    fmt.Sprintf(1,1,auVar2._8_8_,local_18);
    github.com/fatih/color.New();
    knightsquest/renderer.AddMessage();
    *(undefined *)(param_7 + 0x40) = 0;
  }
  *(undefined8 *)(param_8 + 0x38) = 6;
  if (DAT_005884a0 != 0) {
    uVar1 = *(undefined8 *)(param_8 + 0x30);
    runtime.gcWriteBarrier1();
    *in_R11 = uVar1;
    param_8 = extraout_RDX;
  }
  *(undefined **)(param_8 + 0x30) = &DAT_004ba258;
  if (0 < *(long *)(param_7 + 0x18)) {
    return 0;
  }
  github.com/fatih/color.New();
  knightsquest/renderer.AddMessage();
  return 1;
}
/* WARNING: Removing unreachable block (ram,0x00496d15) */
/* WARNING: Removing unreachable block (ram,0x00496d2b) */
/* WARNING: Removing unreachable block (ram,0x00496d1d) */
/* WARNING: Removing unreachable block (ram,0x00496d25) */
/* WARNING: Removing unreachable block (ram,0x00496d2f) */
/* WARNING: Removing unreachable block (ram,0x00496d31) */
/* WARNING: Removing unreachable block (ram,0x00496d39) */
/* WARNING: Removing unreachable block (ram,0x00496d7f) */

void knightsquest/prompt.GetPlayerAction(void)

{
  undefined8 uVar1;
  undefined **ppuVar2;
  long unaff_R14;
  undefined in_XMM15 [16];
  undefined *local_e8;
  undefined **local_e0;
  undefined *local_d8;
  undefined **local_d0;
  undefined *local_c8;
  undefined **local_c0;
  undefined local_b8 [16];
  undefined8 local_a8;
  undefined **local_a0;
  undefined8 local_98 [2];
  undefined local_88 [24];
  undefined8 local_70;
  undefined8 local_68;
  undefined local_60 [88];

  while (uVar1 = DAT_00568300, local_60._8_8_ = in_XMM15._8_8_,
        local_98 <= *(undefined8 **)(unaff_R14 + 0x10)) {
    runtime.morestack_noctxt();
  }
  FUN_0046c710(local_88);
  runtime.makeslice();
  local_b8._0_8_ = FUN_0046c710(&local_e0);
  local_b8._8_8_ = 0x1000;
  local_a8 = 0x1000;
  local_a0 = &PTR_DAT_004e1468;
  local_98[0] = uVar1;
  local_70 = 0xffffffffffffffff;
  local_68 = 0xffffffffffffffff;
  local_60._0_8_ = local_b8._0_8_;
  FUN_0046ca7a(local_60 + 8,local_b8 + 8);
  do {
    while( true ) {
      local_c8 = &DAT_004a2ce0;
      local_c0 = &PTR_s_[attack/defend]_>_004e1370;
      ppuVar2 = &local_c8;
      fmt.Fprint(1,1);
      bufio.(*Reader).ReadString();
      if (ppuVar2 == (undefined **)0x0) break;
      local_d8 = &DAT_004a2ce0;
      local_d0 = &PTR_DAT_004e1380;
      fmt.Fprintln(1,1,&DAT_004a2ce0,&local_d8);
    }
    strings.ToLower();
    strings.TrimSpace();
    local_e8 = &DAT_004a2ce0;
    local_e0 = &PTR_DAT_004e1390;
    fmt.Fprintln(1,1,&DAT_004a2ce0,&local_e8);
  } while( true );
}

void knightsquest/game.(*Game).runGameLoop(void)

{
  byte bVar1;
  char cVar2;
  undefined8 *in_RAX;
  undefined8 *puVar3;
  long lVar4;
  long lVar5;
  undefined8 extraout_RDX;
  byte bVar6;
  long unaff_R14;
  undefined in_XMM15 [16];
  undefined auVar7 [16];
  undefined8 *param_7;
  undefined local_2f8 [40];
  undefined local_2d0 [40];
  undefined local_2a8 [40];
  undefined local_280 [48];
  undefined8 local_250;
  undefined8 local_248;
  undefined8 local_240;
  undefined8 local_238;
  undefined8 local_230;
  undefined8 local_228;
  undefined8 local_220;
  undefined8 local_218;
  undefined8 local_210;
  undefined8 local_208;
  long local_200;
  undefined8 local_1f8;
  undefined8 local_1f0;
  undefined local_1e8 [56];
  undefined local_1b0 [24];
  code *local_198;
  undefined8 local_190;
  undefined local_188 [88];
  undefined *local_130;
  undefined **local_128;
  code *local_120;
  undefined8 local_118;
  code *local_110;
  undefined8 local_108;
  undefined local_100 [16];
  undefined8 local_f0;
  undefined8 *local_e8;
  undefined8 *local_e0;
  undefined local_d8 [16];
  undefined8 local_c8;
  undefined **local_c0;
  undefined8 local_b8;
  undefined local_a8 [24];
  undefined8 local_90;
  undefined8 local_88;
  undefined local_80 [88];
  undefined *local_28;
  undefined **local_20;
  undefined local_18 [16];

  param_7 = in_RAX;
  while (local_280 <= *(undefined **)(unaff_R14 + 0x10)) {
    runtime.morestack_noctxt();
  }
  puVar3 = (undefined8 *)param_7[0xb];
  lVar5 = param_7[0xc];
  while( true ) {
    local_80._8_8_ = in_XMM15._8_8_;
    if (lVar5 < 1) {
      local_d8._0_8_ = *param_7;
      local_e8 = param_7 + 1;
      FUN_0046ca7a(local_d8 + 8);
      FUN_0046ca7a(local_2f8,local_d8 + 8);
      FUN_0046c710(local_2d0);
      knightsquest/renderer.RenderScreen();
      local_208 = 0x20;
      local_190 = github.com/fatih/color.New();
      local_198 = knightsquest/game.(*Game).runGameLoop.(*Color).SprintFunc.func3;
      knightsquest/renderer.AddMessage();
      local_d8._0_8_ = *param_7;
      FUN_0046ca7a(local_d8 + 8,local_e8);
      FUN_0046ca7a(local_2f8,local_d8 + 8);
      FUN_0046c710(local_2d0);
      knightsquest/renderer.RenderScreen();
      local_250 = 0x446b684155444f42;
      local_248 = 0x63374d5a336a4c4d;
      local_240 = 0x31746c4255396f66;
      local_238 = 0x6e4c375942554e41;
      local_230 = 0x384c686770646365;
      local_228 = 0x6236734a595a676d;
      local_220 = 0x657a514d666e6f68;
      local_218 = 0x514c344970736a44;
      lVar5 = runtime.makeslice();
      for (lVar4 = 0; lVar4 < 0x20; lVar4 = lVar4 + 1) {
        bVar1 = (*(byte *)((long)&local_250 + lVar4) ^ *(byte *)((long)&local_230 + lVar4)) % 0x3e;
        bVar6 = bVar1 + 0x41;
        *(byte *)(lVar5 + lVar4) = bVar6;
        if (0x5a < bVar6) {
          if (bVar6 < 0x61) {
            *(byte *)(lVar5 + lVar4) = bVar1 + 0x47;
          }
          else if (0x7a < bVar6) {
            *(byte *)(lVar5 + lVar4) = bVar1 - 10;
          }
        }
      }
      runtime.slicebytetostring();
      local_18._8_8_ = runtime.convTstring();
      local_18._0_8_ = &DAT_004a2ce0;
      fmt.Fprintf(0x25,local_18,&DAT_004a2ce0,&DAT_004c062f,1,1);
      local_28 = &DAT_004a2ce0;
      local_20 = &PTR_s_Press_enter_to_exit_the_game..._004e0e68;
      fmt.Fprintln(1,1,&PTR_s_Press_enter_to_exit_the_game..._004e0e68,&local_28);
      local_f0 = DAT_00568300;
      FUN_0046c710(local_a8);
      runtime.makeslice();
      local_d8._0_8_ = FUN_0046c710(local_100);
      local_d8._8_8_ = 0x1000;
      local_c8 = 0x1000;
      local_c0 = &PTR_DAT_004e1468;
      local_b8 = local_f0;
      local_90 = 0xffffffffffffffff;
      local_88 = 0xffffffffffffffff;
      local_80._0_8_ = local_d8._0_8_;
      FUN_0046ca7a(local_80 + 8,local_d8 + 8);
      bufio.(*Reader).ReadString();
      return;
    }
    local_d8._0_8_ = *puVar3;
    local_200 = lVar5;
    local_e0 = puVar3;
    FUN_0046ca7a(local_d8 + 8,puVar3 + 1);
    local_1f0 = local_d8._0_8_;
    FUN_0046ca7a(local_1e8,local_d8 + 8);
    auVar7 = runtime.convTstring();
    local_100._8_8_ = auVar7._0_8_;
    local_100._0_8_ = &DAT_004a2ce0;
    local_1f8 = fmt.Sprintf(1,1,auVar7._8_8_,local_100);
    local_210 = 0x12;
    local_208 = 0x1f;
    local_108 = github.com/fatih/color.New();
    local_110 = knightsquest/game.(*Game).runGameLoop.(*Color).SprintFunc.func1;
    knightsquest/renderer.AddMessage();
    cVar2 = knightsquest/round.PlayRound();
    local_188._8_8_ = in_XMM15._8_8_;
    if (cVar2 == '\0') break;
    puVar3 = local_e0 + 0xb;
    lVar5 = local_200 + -1;
  }
  local_e8 = param_7 + 1;
  local_d8._0_8_ = *param_7;
  FUN_0046ca7a(local_d8 + 8,local_e8);
  FUN_0046ca7a(local_2f8,local_d8 + 8);
  local_2a8._0_8_ = local_1f0;
  FUN_0046ca7a(local_2a8 + 8,local_1e8);
  knightsquest/renderer.RenderScreen();
  local_208 = 0x1f;
  local_118 = github.com/fatih/color.New();
  local_120 = knightsquest/game.(*Game).runGameLoop.(*Color).SprintFunc.func2;
  knightsquest/renderer.AddMessage();
  local_d8._0_8_ = *param_7;
  FUN_0046ca7a(local_d8 + 8,local_e8);
  FUN_0046ca7a(local_2f8,local_d8 + 8);
  local_2a8._0_8_ = local_1f0;
  FUN_0046ca7a(local_2a8 + 8,local_1e8);
  knightsquest/renderer.RenderScreen();
  local_130 = &DAT_004a2ce0;
  local_128 = &PTR_s_Press_enter_to_exit_the_game..._004e0e68;
  fmt.Fprintln(1,1,extraout_RDX,&local_130);
  local_f0 = DAT_00568300;
  FUN_0046c710(local_1b0);
  runtime.makeslice();
  local_d8._0_8_ = FUN_0046c710(local_100);
  local_d8._8_8_ = 0x1000;
  local_c8 = 0x1000;
  local_c0 = &PTR_DAT_004e1468;
  local_b8 = local_f0;
  local_90 = 0xffffffffffffffff;
  local_88 = 0xffffffffffffffff;
  local_188._0_8_ = local_d8._0_8_;
  FUN_0046ca7a(local_188 + 8,local_d8 + 8);
  bufio.(*Reader).ReadString();
  return;
}
```

Add back stpes here from gpt
```python

local_250 = 0x446b684155444f42;
local_248 = 0x63374d5a336a4c4d;
local_240 = 0x31746c4255396f66;
local_238 = 0x6e4c375942554e41;
local_230 = 0x384c686770646365;
local_228 = 0x6236734a595a676d;
local_220 = 0x657a514d666e6f68;
local_218 = 0x514c344970736a44;
This sequence of variables holds hexadecimal values that likely correspond to parts of the encoded flag.

Then there's a loop that processes these values:
lVar5 = runtime.makeslice();
for (lVar4 = 0; lVar4 < 0x20; lVar4 = lVar4 + 1) {
    bVar1 = (*(byte *)((long)&local_250 + lVar4) ^ *(byte *)((long)&local_230 + lVar4)) % 0x3e;
    bVar6 = bVar1 + 0x41;
    *(byte *)(lVar5 + lVar4) = bVar6;
    if (0x5a < bVar6) {
        if (bVar6 < 0x61) {
            *(byte *)(lVar5 + lVar4) = bVar1 + 0x47;
        }
        else if (0x7a < bVar6) {
            *(byte *)(lVar5 + lVar4) = bVar1 - 10;
        }
    }
}
runtime.slicebytetostring();
This code is generating a 32-character string, which is likely the flag you need.

Step 2: Extract and Convert the Constants
You can extract the hexadecimal values and convert them to bytes. Here's how you can do it:

List the Constants:

plaintext
Copy code
local_250: 0x446b684155444f42
local_248: 0x63374d5a336a4c4d
local_240: 0x31746c4255396f66
local_238: 0x6e4c375942554e41
local_230: 0x384c686770646365
local_228: 0x6236734a595a676d
local_220: 0x657a514d666e6f68
local_218: 0x514c344970736a44
Convert the Hex Values to Byte Arrays:

For each of these 64-bit integers, convert them to 8 bytes in little-endian order.

For example, for local_250:

python
Copy code
import struct

local_250 = struct.pack('<Q', 0x446b684155444f42)
Repeat this for each variable.

Step 3: Concatenate the Byte Arrays
Once you have the byte arrays for all variables, concatenate them to form two large byte arrays:

First Array (array1): Concatenate local_250, local_248, local_240, and local_238.
Second Array (array2): Concatenate local_230, local_228, local_220, and local_218.
Step 4: Implement the Flag Generation Logic
Now, replicate the loop logic in a script to generate the flag.

Here's a step-by-step guide:

Initialize the Arrays:

python
Copy code
array1 = b''  # Concatenate bytes from local_250 to local_238
array2 = b''  # Concatenate bytes from local_230 to local_218
Perform the XOR and Modulo Operations:

python
Copy code
flag_bytes = bytearray()
for i in range(32):
    b1 = array1[i]
    b2 = array2[i]
    bVar1 = (b1 ^ b2) % 0x3E
    bVar6 = bVar1 + 0x41
    if bVar6 > 0x5A:
        if bVar6 < 0x61:
            bVar6 = bVar1 + 0x47
        elif bVar6 > 0x7A:
            bVar6 = bVar1 - 10
    flag_bytes.append(bVar6)
Convert the Flag Bytes to a String:

python
Copy code
flag = flag_bytes.decode('ascii')
print("Flag:", flag)
Step 5: Run the Script to Obtain the Flag
By running this script, you'll get the flag without needing to defeat the monster in the game.

Why This Approach Works
The monster is designed to be unbeatable through normal gameplay due to its inflated stats.
The challenge expects you to reverse engineer the binary to find an alternative way to obtain the flag.
By analyzing the code that generates the flag, you can extract it directly.
Additional Tips
Verify Endianness: Ensure that you're using the correct byte order when converting the hex values to bytes. Go uses little-endian format.
Edge Cases in Character Conversion: Pay attention to the conditional statements adjusting bVar6 to ensure the resulting characters are valid ASCII letters.
Sample Code Snippet
Here's a Python script outline to help you get started:

```
```python
python
Copy code
import struct

# Define the constants
local_250 = struct.pack('<Q', 0x446b684155444f42)
local_248 = struct.pack('<Q', 0x63374d5a336a4c4d)
local_240 = struct.pack('<Q', 0x31746c4255396f66)
local_238 = struct.pack('<Q', 0x6e4c375942554e41)

local_230 = struct.pack('<Q', 0x384c686770646365)
local_228 = struct.pack('<Q', 0x6236734a595a676d)
local_220 = struct.pack('<Q', 0x657a514d666e6f68)
local_218 = struct.pack('<Q', 0x514c344970736a44)

# Concatenate the bytes
array1 = local_250 + local_248 + local_240 + local_238
array2 = local_230 + local_228 + local_220 + local_218

# Generate the flag
flag_bytes = bytearray()
for i in range(32):
    b1 = array1[i]
    b2 = array2[i]
    bVar1 = (b1 ^ b2) % 0x3E
    bVar6 = bVar1 + 0x41
    if bVar6 > 0x5A:
        if bVar6 < 0x61:
            bVar6 = bVar1 + 0x47
        elif bVar6 > 0x7A:
            bVar6 = bVar1 - 10
    flag_bytes.append(bVar6)

flag = flag_bytes.decode('ascii')
print("Flag:", flag)
Note: Replace the placeholder code with actual values and logic based on your analysis.

Conclusion
By reverse engineering the game's binary and analyzing the flag generation code, you can obtain the flag without modifying the monster's stats or game logic. This approach aligns with typical reverse engineering challenges in Capture The Flag (CTF) competitions.

Feel free to ask if you need further clarification on any of the steps!
```

All we needed was to decode this function
```python
import struct

# Define the constants (converted to little-endian byte arrays)
local_250 = struct.pack('<Q', 0x446b684155444f42)
local_248 = struct.pack('<Q', 0x63374d5a336a4c4d)
local_240 = struct.pack('<Q', 0x31746c4255396f66)
local_238 = struct.pack('<Q', 0x6e4c375942554e41)

local_230 = struct.pack('<Q', 0x384c686770646365)
local_228 = struct.pack('<Q', 0x6236734a595a676d)
local_220 = struct.pack('<Q', 0x657a514d666e6f68)
local_218 = struct.pack('<Q', 0x514c344970736a44)

# Concatenate the bytes to form two arrays
array1 = local_250 + local_248 + local_240 + local_238
array2 = local_230 + local_228 + local_220 + local_218

# Generate the flag
flag_bytes = bytearray()
for i in range(32):
    b1 = array1[i]
    b2 = array2[i]
    bVar1 = (b1 ^ b2) % 0x3E  # XOR and modulo operation
    bVar6 = bVar1 + 0x41  # Offset to ASCII range

    # Adjust values based on conditions
    if bVar6 > 0x5A:
        if bVar6 < 0x61:
            bVar6 = bVar1 + 0x47
        elif bVar6 > 0x7A:
            bVar6 = bVar1 - 10

    # Append the result to flag_bytes
    flag_bytes.append(bVar6)

# Convert the byte array to a string to get the flag
flag = flag_bytes.decode('ascii')
print("Flag:", flag)

```

*[image unavailable]*

*[image unavailable]*

I definitely cheesed chatgpt for the script on this one, curl post the key and get the flag

*[image unavailable]*

```python
curl -X POST -H "Content-Type: application/json" -d '{"password":"hmafgAhAalqmQABBOAZtP3OWFegsQDAB"}' http://challenge.ctf.games:31235/submit

{"flag":"flag{40b5b7e5395ee921cbbc804d4350b9c1}"}
```

*[image unavailable]*
