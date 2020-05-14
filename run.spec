# -*- mode: python ; coding: utf-8 -*-
import sys
import os.path as osp
sys.setrecursionlimit(5000)

block_cipher = None

SETUP_DIR = 'E:\\WorkSpace\\Python\\737NG_CDU\\Version_1\\'

block_cipher = None


a = Analysis([SETUP_DIR+'CDU.py',
			  SETUP_DIR+'config.py',
			  SETUP_DIR+'dataFile.py',
			  SETUP_DIR+'logger.py',
			  SETUP_DIR+'run.py',
			  SETUP_DIR+'settings.py',
			  SETUP_DIR+'logic\\drawLogic.py',
			  SETUP_DIR+'logic\\inputLogic.py',
			  SETUP_DIR+'logic\\pageLogic.py',
			  SETUP_DIR+'DataFiles\\NavAIRPORT.py',
			  SETUP_DIR+'DataFiles\\NavAIRPORTS.py',
			  SETUP_DIR+'DataFiles\\NavIDENT.py',
			  SETUP_DIR+'DataFiles\\NavRTE.py',
			  ],
             pathex=['E:\\WorkSpace\\Python\\737NG_CDU\\Version_1\\'],
             binaries=[],
             datas=[(SETUP_DIR+'Database','Database'),
			        (SETUP_DIR+'Resource','Resource')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='FYCYC-CDU-737NG',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='FYCYC-CDU-737NG')
