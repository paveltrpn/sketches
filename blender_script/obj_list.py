from typing import Optional
import bpy
from bpy.types import bpy_struct
import mathutils

foo = mathutils.Vector()

class CBpyCamera:
    def __init__(self, cmr: bpy.types.Object) -> None:
        self.cmrLocation = mathutils.Vector((cmr.location[0], cmr.location[1], cmr.location[2]))
        self.cmrEuler = mathutils.Vector((cmr.rotation_euler[0], cmr.rotation_euler[1], cmr.rotation_euler[2]))

class CSceneEntities:
    def __init__(self) -> None:
        self.scMeshes = list()
        self.scCameras = list()
        self.scLights = list()

        scene_entities = bpy.data.objects

        for obj in scene_entities:
            if obj.type == "CAMERA":
                self.scCameras.append(obj)
            
            if obj.type == "LIGHT":
                self.scLights.append(obj)
            
            if obj.type == "MESH":
                self.scMeshes.append(obj)

        self.scCamerasCnt = len(self.scCameras)
        self.scLightsCnt = len(self.scLights)
        self.scMeshesCnt = len(self.scMeshes)

    def printSceneStats(self) -> None:
        print("scene entities stat: Meshes - {}, Lights - {}, Cameras - {}".format(self.scMeshesCnt, self.scLightsCnt, self.scCamerasCnt))

    def findMesh(self, name: str) -> Optional[bpy.types.Mesh]:
        if self.scMeshesCnt != 0:
            for obj in self.scMeshes:
                if obj.name == name:
                    return obj
            print("CSceneEntities.findMesh(): error! no Mesh with name {} in scene!".format(name))
        else:
            print("CSceneEntities.findMesh(): error! no Meshes in scene!")
            return None

    def findLight(self, name: str) -> Optional[bpy.types.Object]:
        if self.scLightsCnt != 0:
            for obj in self.scLights:
                if obj.name == name:
                    return obj
            print("CSceneEntities.findLight(): error! no Light with name {} in scene!".format(name))
        else:
            print("CSceneEntities.findLight(): error! no Lights in scene!")
            return None

    def findCamera(self, name: str) -> Optional[bpy.types.Object]:
        if self.scCamerasCnt != 0:
            for obj in self.scCameras:
                if obj.name == name:
                    return obj
            print("CSceneEntities.findCamera(): error! no Camera with name {} in scene!".format(name))
        else:
            print("CSceneEntities.findCamera(): error! no Cameras in scene!")
            return None

def exportCamera(cmr: bpy.types.Object) -> None:
    if isinstance(cmr, bpy.types.Object):
        print("exportCamera(): camera {} stats".format(cmr.name))
        print(cmr.location)
        print(cmr.rotation_euler)
    else:
        print("exportCamera(): it's not a Camera!")
        return

def printMeshVertices(bar: bpy.types.Object) -> None:
    mtrx = bar.matrix_world
    me = bar.data
    
    print("Vert coords:")
    for vert in me.vertices:
        glob_vert = mtrx @ vert.co
        print("{0:.3f} {0:.3f} {0:.3f}".format(glob_vert.x, glob_vert.y, glob_vert.z))

def printMeshData(bar: bpy.types.Object) -> None:
    me = bar.data

    for poly in me.polygons:
        print("Polygon: {}, length: {}".format(poly.index, poly.loop_total))
        # print(poly.normal)
        # range is used here to show how the polygons reference loops,
        # for convenience 'poly.loop_indices' can be used instead.
        print("vertex id's:")

        for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
            print("{} ".format(me.loops[loop_index].vertex_index), end=" ")
        
        print("")

def printMeshDataTriang(bar: bpy.types.Object) -> None:
    me = bar.data
    me.calc_loop_triangles()

    for poly in me.loop_triangles:
        print("Polygon: {}".format(poly.index))
        # print(poly.normal)
        # range is used here to show how the polygons reference loops,
        # for convenience 'poly.loop_indices' can be used instead.
        print("vertex id's:")

        for loop_index in range(3):
            print("{} ".format(me.loops[loop_index].vertex_index), end=" ")
        
        print("")

def printMeshUV(bar: bpy.types.Object) -> None:
    me = bar.data

    uv_layer = me.uv_layers.active.data

    for poly in me.polygons:
        print("Polygon: {}, length: {}".format(poly.index, poly.loop_total))

        print("UV coords:")

        for loop_index in range(poly.loop_start, poly.loop_start + poly.loop_total):
            print("U:{0:.3f} V:{0:.3f}".format(uv_layer[loop_index].uv.x, uv_layer[loop_index].uv.y))

        print("")

def printMeshUVTriang(bar: bpy.types.Object) -> None:
    me = bar.data
    me.calc_loop_triangles()

    uv_layer = me.uv_layers.active.data

    for poly in me.loop_triangles:
        print("Polygon: {}".format(poly.index))
        
        print("UV coords:")

        for loop_index in range(3):
            print("U:{0:.3f} V:{0:.3f}".format(uv_layer[loop_index].uv.x, uv_layer[loop_index].uv.y))

        print("")

def main() -> None:
    entities = CSceneEntities()

    entities.printSceneStats()

    # cmr = entities.findCamera("Camera")
    # exportCamera(cmr)
# 
    # foo = CBpyCamera(cmr)
    # print(foo.cmrEuler)

    bar = entities.findMesh("Cube")
    # printMeshVertices(bar)
    # printMeshData(bar)
    # printMeshDataTriang(bar)
    printMeshUV(bar)
    # printMeshUVTriang(bar)

if __name__ == "__main__":
    main()