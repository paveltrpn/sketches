
import bpy
from bpy.types import Operator, Panel, PropertyGroup
from bpy.utils import register_class, unregister_class
from bpy.props import BoolProperty

# Весь тутор отсюда - https://www.youtube.com/watch?v=3Bw4Re-7HLY

# Класс панели. Имя класса должно быть именно
# в таком формате - т.е. слдержать "__PT__..."
class OBJECT_PT_TestPanel(Panel):
    bl_label = "Test Panel"
    bl_space_type = "VIEW_3D" # на каком окне отображается панель
    bl_region_type = "UI"   # Регион, где отображается панель
    bl_category = "Test Panel Horisontal"

    def draw(self, context):
        layout = self.layout

# Classes, registerClass(), unregisterClass() - это бйлерплейт для
# регистрации новых панелий и инструментов (аддонов) в Blender 
classes = [OBJECT_PT_TestPanel]

def registerClass() -> None:
    for cl in classes:
        register_class(cl)

def unregisterClass() -> None:
    for cl in reversed(classes):
        unregister_class(cl)

def main() -> None:
    print("{}".format("Hello blender!"))
    registerClass()

if __name__ == "__main__":
    main()