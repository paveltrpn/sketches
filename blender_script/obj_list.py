from typing import Optional
import bpy
from bpy.types import bpy_struct
import mathutils

camera = bpy.context.scene.camera

foo = mathutils.Vector()

class CBpyCamera:
    def __init__(self, cmr: bpy_struct) -> None:
        self.cmrLocation: mathutils.Vector(cmr.location[0], cmr.location[1], cmr.location[2])
        self.cmrEuler = cmr.rotation_euler

class CSceneEntities:
    def __init__(self) -> None:
        self.scMeshes = list()
        self.scCameras = list()
        self.scLights = list()

        scene_entities = bpy.data.objects[0]

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

    def findMesh(self, name: str) -> Optional[bpy_struct]:
        if self.scMeshesCnt != 0:
            for obj in self.scMeshes:
                if obj.name == name:
                    return obj
            print("CSceneEntities.findMesh(): error! no Mesh with name {} in scene!".format(name))
        else:
            print("CSceneEntities.findMesh(): error! no Meshes in scene!")
            return None

    def findLight(self, name: str) -> Optional[bpy_struct]:
        if self.scLightsCnt != 0:
            for obj in self.scLights:
                if obj.name == name:
                    return obj
            print("CSceneEntities.findLight(): error! no Light with name {} in scene!".format(name))
        else:
            print("CSceneEntities.findLight(): error! no Lights in scene!")
            return None

    def findCamera(self, name: str) -> Optional[bpy_struct]:
        if self.scCamerasCnt != 0:
            for obj in self.scCameras:
                if obj.name == name:
                    return obj
            print("CSceneEntities.findCamera(): error! no Camera with name {} in scene!".format(name))
        else:
            print("CSceneEntities.findCamera(): error! no Cameras in scene!")
            return None

def exportCamera(cmr: bpy.context.scene.camera) -> None:
    if isinstance(cmr, bpy_struct):
        print("exportCamera(): camera {} stats".format(cmr.name))
        print(cmr.location)
        print(cmr.rotation_euler)
    else:
        print("exportCamera(): it's not a Camera!")
        return
        
def main() -> None:
    entities = CSceneEntities()

    entities.printSceneStats()

    cmr = entities.findCamera("Camera2")
    exportCamera(cmr)

if __name__ == "__main__":
    main()