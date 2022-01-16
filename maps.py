source_joints = ['hips', 'LowerBack', 'spine', 'chest', 'neck', 'head', 'shoulder.L', 
'upper_arm.L', 'forearm.L', 'hand.L', 'palm.01.L', 'f_index.01.L', 'f_index.02.L', 
'f_index.03.L', 'thumb.01.L', 'thumb.02.L', 'thumb.03.L', 'palm.02.L', 
'f_middle.01.L', 'f_middle.02.L', 'f_middle.03.L', 'palm.03.L', 'f_ring.01.L', 
'f_ring.02.L', 'f_ring.03.L', 'palm.04.L', 'f_pinky.01.L', 'f_pinky.02.L', 
'f_pinky.03.L', 'shoulder.R', 'upper_arm.R', 'forearm.R', 'hand.R', 'palm.01.R', 
'f_index.01.R', 'f_index.02.R', 'f_index.03.R', 'thumb.01.R', 'thumb.02.R', 
'thumb.03.R', 'palm.02.R', 'f_middle.01.R', 'f_middle.02.R', 'f_middle.03.R', 
'palm.03.R', 'f_ring.01.R', 'f_ring.02.R', 'f_ring.03.R', 'palm.04.R', 
'f_pinky.01.R', 'f_pinky.02.R', 'f_pinky.03.R', 'pelvis.L', 'thigh.L', 
'shin.L', 'foot.L', 'toe.L', 'heel.L', 'heel.02.L', 'pelvis.R', 
'thigh.R', 'shin.R', 'foot.R', 'toe.R', 'heel.R', 'heel.02.R']

target_joints = ['Hips', 'Spine', 'Spine1', 'Spine2', 'Neck', 'Head',
'LeftShoulder', 'LeftArm', 'LeftForeArm', 'LeftHand',
'RightShoulder', 'RightArm', 'RightForeArm', 'RightHand', 
'LeftUpLeg', 'LeftLeg', 'LeftFoot', 'LeftToeBase', 
'RightUpLeg', 'RightLeg', 'RightFoot', 'RightToeBase']

mapping = {
    'Hips': 'hips',
    'Spine': 'LowerBack',
    'Spine1': 'spine',
    'Spine2': 'chest',
    'Neck': 'neck',
    'Head':'head',
    'LeftShoulder':'shoulder.R',
    'LeftArm': 'upper_arm.R',
    'LeftForeArm': 'forearm.R',
    'LeftHand': 'hand.R',
    'RightShoulder': 'shoulder.L',
    'RightArm': 'upper_arm.L',
    'RightForeArm': 'forearm.L',
    'RightHand': 'hand.L',
    'LeftUpLeg' : 'thigh.R',
    'LeftLeg': 'shin.R',
    'LeftFoot': 'foot.R',
    'LeftToeBase' : 'toe.R',
    'RightUpLeg': 'thigh.L',
    'RightLeg': 'shin.L',
    'RightFoot': 'foot.L',
    'RightToeBase': 'toe.L',

}

idx_source = {v: source_joints.index(v) for v in mapping.values()}
idx_target = {target_joints.index(k): k for k in mapping.keys()}

def get_dofs():
    with open('data/estimated_animation.bvh') as f:
        src_data = f.readlines()
    dof_dict = {}
    for joint in source_joints:
        for i, l in enumerate(src_data):
            if joint in l:
                dof = src_data[i+3].split(' ')[1]
                dof_dict[joint] = int(dof)
    
    return dof_dict




def get_rot_ids():
    rot_ids = {}
    prev = 0
    for joint in source_joints:
        dof = prev + (0 if dofs[joint] == 3 else 3)
        prev=dof+3
        rot_ids[joint] = dof
    return rot_ids


def get_orientations():
    with open('data/estimated_animation.bvh') as f:
        src_data = f.readlines()
    orientations_dict = {}
    for joint in source_joints:
        for i, l in enumerate(src_data):
            if joint in l:
                dof = src_data[i+3].split(' ')[1]
                if int(dof) == 3:
                    orientation = src_data[i+3].split(' ')[2:5]
                else:
                    orientation = src_data[i+3].split(' ')[5:8]
                
                zxy = [0, 0, 0]
        
                for ore_id, ore in enumerate(orientation):
                    
                    if ore[0] == 'X':
                        zxy[1] = ore_id
                    if ore[0] == 'Y':
                        zxy[2] = ore_id
                    if ore[0] == 'Z':                        
                        zxy[0] = ore_id
                print(orientation, zxy)
                orientations_dict[joint] = zxy
    return orientations_dict

dofs = get_dofs()
rot_ids = get_rot_ids()
orientations_dict = get_orientations()
                
if __name__ == '__main__':
    # from bvh import Bvh
    # with open('data/estimated_animation.bvh') as f:
    #     mocap = Bvh(f.read())
    # print(len(mocap.get_joints_names()))

    # with open('data/estimated_animation.bvh') as f:
    #     src_data = f.readlines()
    # count = 0
    # for l in src_data:
    #     if 'JOINT' in l:
    #         print(l)
    #         count += 1
    # print(count)
 
    # print(len(source_joints), len(target_joints))
    # for k, v in mapping.items():
    #     print(k in target_joints, v in source_joints)
    #     print(idx_source)
    #     print(idx_target)
    #     print(len(target_joints), len(mapping.keys()))

    # print(target_joints[14], source_joints[52])

    # get_dofs()
    # get_rot_ids()
    # print(orientations_dict)
    print(dofs)
    print()
    print(rot_ids)
    print()
    print(orientations_dict)