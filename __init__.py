bl_info = {
    'name': 'SourceOps',
    'author': 'bonjorno7, Almaas, Cabbage McGravel, Gorange, Krystian, RED_EYE, SethTooQuick, Yonder',
    'description': 'A more convenient alternative to Blender Source Tools',
    'blender': (2, 83, 0),
    'version': (0, 6, 4),
    'location': '3D View > Sidebar',
    'category': 'Import-Export',
}


from . import addon


def register():
    addon.register()


def unregister():
    addon.unregister()
