# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['3_label.py'],
             pathex=['C:\\Users\\hj144\\Desktop\\Coding\\Python\\GUI_project\\Gui_Grammer'],
             binaries=[],
             datas=[('.\\3_images\\*.png', '3_images')],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='3_label',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False )
