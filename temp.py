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
    'LeftShoulder':'shoulder.L',
    'LeftArm': 'upper_arm.L',
    'LeftForeArm': 'forearm.L',
    'LeftHand': 'hand.L',
    'RightShoulder': 'shoulder.R',
    'RightArm': 'upper_arm.R',
    'RightForeArm': 'forearm.R',
    'RightHand': 'hand.R',
    'LeftUpLeg' : 'thigh.L',
    'LeftLeg': 'shin.L',
    'LeftFoot': 'foot.L',
    'LeftToeBase' : 'toe.L',
    'RightUpLeg': 'thigh.R',
    'RightLeg': 'shin.R',
    'RightFoot': 'foot.R',
    'RightToeBase': 'toe.R',

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
    
    return dofs_dict

dofs = get_dofs()
dofs = {'hips': 6, 'LowerBack': 3, 'spine': 3, 'chest': 3, 'neck': 3, 'head': 6, 
'shoulder.L': 6, 'upper_arm.L': 6, 'forearm.L': 3, 'hand.L': 3, 'palm.01.L': 6,
'f_index.01.L': 3, 'f_index.02.L': 3, 'f_index.03.L': 3, 'thumb.01.L': 6,
'thumb.02.L': 3, 'thumb.03.L': 3, 'palm.02.L': 6, 'f_middle.01.L': 3, 'f_middle.02.L': 3, 
'f_middle.03.L': 3, 'palm.03.L': 6, 'f_ring.01.L': 3, 'f_ring.02.L': 3, 'f_ring.03.L': 3,
'palm.04.L': 6, 'f_pinky.01.L': 3, 'f_pinky.02.L': 3, 'f_pinky.03.L': 3, 'shoulder.R': 6,
'upper_arm.R': 6, 'forearm.R': 3, 'hand.R': 3, 'palm.01.R': 6, 'f_index.01.R': 3,
'f_index.02.R': 3, 'f_index.03.R': 3, 'thumb.01.R': 6, 'thumb.02.R': 3, 'thumb.03.R': 3, 
'palm.02.R': 6, 'f_middle.01.R': 3, 'f_middle.02.R': 3, 'f_middle.03.R': 3, 'palm.03.R': 6, 
'f_ring.01.R': 3, 'f_ring.02.R': 3, 'f_ring.03.R': 3, 'palm.04.R': 6, 'f_pinky.01.R': 3, 
'f_pinky.02.R': 3, 'f_pinky.03.R': 3, 'pelvis.L': 6, 'thigh.L': 3, 'shin.L': 3, 'foot.L': 3, 
'toe.L': 3, 'heel.L': 3, 'heel.02.L': 6, 'pelvis.R': 6, 
'thigh.R': 3, 'shin.R': 3, 'foot.R': 3, 'toe.R': 3, 'heel.R': 3, 'heel.02.R': 6}

def get_rot_ids():
    rot_ids = {}
    prev = 0
    for joint in source_joints:
        dof = prev + (0 if dofs[joint] == 3 else 3)
        prev=dof+3
        rot_ids[joint] = dof
    print(rot_ids)

rot_ids = {'hips': 3, 'LowerBack': 6, 'spine': 9, 'chest': 12, 'neck': 15, 'head': 21, 'shoulder.L': 27, 
'upper_arm.L': 33, 'forearm.L': 36, 'hand.L': 39, 'palm.01.L': 45, 'f_index.01.L': 48, 'f_index.02.L': 51,
'f_index.03.L': 54, 'thumb.01.L': 60, 'thumb.02.L': 63, 'thumb.03.L': 66, 'palm.02.L': 72, 'f_middle.01.L': 75,
'f_middle.02.L': 78, 'f_middle.03.L': 81, 'palm.03.L': 87, 'f_ring.01.L': 90, 'f_ring.02.L': 93, 'f_ring.03.L': 96,
'palm.04.L': 102, 'f_pinky.01.L': 105, 'f_pinky.02.L': 108, 'f_pinky.03.L': 111, 'shoulder.R': 117,
'upper_arm.R': 123, 'forearm.R': 126, 'hand.R': 129, 'palm.01.R': 135, 'f_index.01.R': 138, 'f_index.02.R': 141,
'f_index.03.R': 144, 'thumb.01.R': 150, 'thumb.02.R': 153, 'thumb.03.R': 156, 'palm.02.R': 162, 'f_middle.01.R': 165,
'f_middle.02.R': 168, 'f_middle.03.R': 171, 'palm.03.R': 177, 'f_ring.01.R': 180, 'f_ring.02.R': 183, 'f_ring.03.R': 186,
'palm.04.R': 192, 'f_pinky.01.R': 195, 'f_pinky.02.R': 198, 'f_pinky.03.R': 201, 'pelvis.L': 207, 'thigh.L': 210, 'shin.L': 213,
'foot.L': 216, 'toe.L': 219, 'heel.L': 222, 'heel.02.L': 228, 
'pelvis.R': 234, 'thigh.R': 237, 'shin.R': 240, 'foot.R': 243, 'toe.R': 246, 'heel.R': 249, 'heel.02.R': 255}

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
    print(orientations_dict)

orientations_dict = {'hips': [2, 0, 1], 'LowerBack': [2, 0, 1], 'spine': [2, 0, 1], 'chest': [2, 0, 1],
'neck': [2, 0, 1], 'head': [2, 0, 1], 'shoulder.L': [2, 1, 0], 'upper_arm.L': [2, 0, 1], 'forearm.L': [2, 0, 1],
'hand.L': [2, 0, 1], 'palm.01.L': [2, 1, 0], 'f_index.01.L': [2, 0, 1], 'f_index.02.L': [2, 0, 1], 'f_index.03.L': [2, 0, 1],
'thumb.01.L': [2, 0, 1], 'thumb.02.L': [2, 0, 1], 'thumb.03.L': [2, 0, 1], 'palm.02.L': [2, 1, 0], 'f_middle.01.L': [2, 0, 1],
'f_middle.02.L': [2, 0, 1], 'f_middle.03.L': [2, 0, 1], 'palm.03.L': [2, 1, 0], 'f_ring.01.L': [2, 0, 1], 'f_ring.02.L': [2, 0, 1],
'f_ring.03.L': [2, 0, 1], 'palm.04.L': [2, 1, 0], 'f_pinky.01.L': [2, 0, 1], 'f_pinky.02.L': [2, 0, 1], 'f_pinky.03.L': [2, 0, 1],
'shoulder.R': [2, 1, 0], 'upper_arm.R': [2, 0, 1], 'forearm.R': [2, 0, 1], 'hand.R': [2, 0, 1], 'palm.01.R': [2, 1, 0],
'f_index.01.R': [2, 0, 1], 'f_index.02.R': [2, 0, 1], 'f_index.03.R': [2, 0, 1], 'thumb.01.R': [2, 0, 1], 'thumb.02.R': [2, 0, 1],
'thumb.03.R': [2, 0, 1], 'palm.02.R': [2, 1, 0], 'f_middle.01.R': [2, 0, 1], 'f_middle.02.R': [2, 0, 1], 'f_middle.03.R': [2, 0, 1],
'palm.03.R': [2, 1, 0], 'f_ring.01.R': [2, 0, 1], 'f_ring.02.R': [2, 0, 1], 'f_ring.03.R': [2, 0, 1], 'palm.04.R': [2, 1, 0],
'f_pinky.01.R': [2, 0, 1], 'f_pinky.02.R': [2, 0, 1], 'f_pinky.03.R': [2, 0, 1], 'pelvis.L': [2, 0, 1], 'thigh.L': [2, 0, 1],
'shin.L': [2, 0, 1], 'foot.L': [2, 0, 1], 'toe.L': [2, 0, 1], 'heel.L': [2, 0, 1], 'heel.02.L': [2, 0, 1], 'pelvis.R': [2, 0, 1], 
'thigh.R': [2, 0, 1], 'shin.R': [2, 0, 1], 'foot.R': [2, 0, 1], 'toe.R': [2, 0, 1], 'heel.R': [2, 0, 1], 'heel.02.R': [2, 0, 1]}
                
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
    get_orientations()