
import bpy
from bpy.types import Scene, bpy_struct
import mathutils

def main() -> None:
    print("toogle mode - {}".format(bpy.context.mode))

    for obj in bpy.data.objects:
        print("type - {} name - {}".format(obj.type, obj.name))
        scnObjList = []
        scnObjList.append(obj.name)

    foo = bpy.data.objects[scnObjList[0]]
    print(foo.type)

    bpy.ops.object.editmode_toggle()
    print("toogle mode - {}".format(bpy.context.mode))

if __name__ == "__main__":
    print("")
    main()
