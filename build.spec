# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['__main__.py'],
             pathex=['C:\\Users\\andrew\\alpha-video'],
             binaries=[],
             datas=[('*', '.')],
             hiddenimports=[],
             hookspath=['c:\\users\\andrew\\appdata\\local\\programs\\python\\python37\\lib\\site-packages\\pyupdater\\hooks'],
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
          name='alpha-video',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True , icon='logo.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='alpha-video')
