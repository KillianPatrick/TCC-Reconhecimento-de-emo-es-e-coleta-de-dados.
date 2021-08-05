# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['facialExpressionRecognition.py', 'grafPlot.py', 'gui.py', 'reportFile.py'],
             pathex=['C:\\Users\\Pichau\\Desktop\\TCC\\TCCreconhecimento'],
             binaries=[],
             datas=[('facial_expression_model_structure_dot_online.json', '.'), ('facial_expression_model_weights_dot_online.h5', '.'), ('haarcascade_frontalface_default.xml', '.')],
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
          name='facialExpressionRecognition',
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
               name='facialExpressionRecognition')
