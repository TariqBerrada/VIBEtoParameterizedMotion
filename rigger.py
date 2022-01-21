# Okay so now I have the correct joint mappings.
# What remains to be done is to find the indices of every element in the dictionary and transfer the rotation values from the source bvh to the target bvh.
from maps import source_joints, idx_source, idx_target, source_joints, target_joints, mapping, rot_ids, orientations_dict

print(source_joints)
print(idx_source)
print(idx_target)
print('source', len(source_joints), ' | target : ', len(target_joints))

def transfer_rot(source_dir, target_dir, output_dir):
    source_bvh = open(source_dir).readlines()
    target_bvh = open(target_dir).readlines()
    
    # get source and target separators.
    for i, l in enumerate(source_bvh):
        if l[:10] == "Frame Time":
            sep_src = i

    for i, l in enumerate(target_bvh):
        if l[:10] == "Frame Time":
            sep_tar = i

    print('src %d - tar %d'%(sep_src, sep_tar))
    
    # loop over the source frames and add send the rotations to the target anim.
    for i in range(sep_src+1, len(source_bvh)): # her I assume the source less frames than the target
        j = i - sep_src + sep_tar
        if j == len(target_bvh) - 1:
            break
        
        src_frame = source_bvh[i].split(' ')
        tar_frame = target_bvh[j].split(' ')
        print('length of frames', len(src_frame), len(tar_frame))
        # loop over each rotation value in the target frame animation.
        for k in range(3, len(tar_frame)-1, 3):
            tar_idx = (k-3)//3 # source index while k is the index in the rotations anim.
            
            tar_joint = idx_target[tar_idx]
            src_joint = mapping[tar_joint]
            if False: #tar_idx == 0:
                pelvis_l_id = source_joints.index('pelvis.L')
                pelvis_r_id = source_joints.index('pelvis.R')
                hip_id = source_joints.index('hips')
                o = [2, 0, 1]
                p1 = src_frame[pelvis_l_id:pelvis_l_id+3]
                p2 = src_frame[pelvis_r_id:pelvis_r_id+3]
                p3 = src_frame[hip_id:hip_id+3]
                
                for _i in range(3):
                    p1[_i] = float(p1[_i])
                    p2[_i] = float(p2[_i])
                    p3[_i] = float(p3[_i])
                    # print('sum test', p1[_i], p2[_i], p3[_i], (p1[_i]+p2[_i]+p3[_i])/3)
                # print('int', p1, p2, p3)

                
                pelvis = [(p1[o[0]]+p2[o[0]]+p3[o[0]])/3, (p1[o[1]]+p2[o[1]]+p3[o[1]])/3, (p1[o[2]]+p2[o[2]]+p3[o[2]])/3]

                for _i in range(3):
                    pelvis[_i] = str(pelvis[_i])
                print(p1, p2, p3, pelvis)
                tar_frame[k:k+3] = pelvis
            else:
                idx_out = rot_ids[src_joint] # to get the correct positions of z, x and y axis.

                o = orientations_dict[src_joint]
                rot = src_frame[idx_out:idx_out+3]
                
                aligned_rot = [rot[o[0]], rot[o[1]], rot[o[2]]]
                # align rotations axis for arms and forearms
                if tar_joint in ['LeftArm', 'LeftForeArm', 'RightArm', 'RightForeArm']:
                    print('ooooooooo', o)
                    for u in range(2,3): # only flip z and x
                        if aligned_rot[u][0] == '-':
                            aligned_rot[u] = aligned_rot[u][1:]
                        else:
                            aligned_rot[u] = '-' + aligned_rot[u]
                
                # if aligned_rot[1][0] == '-':
                #     aligned_rot[1] = aligned_rot[1][1:]
                # else:
                #     aligned_rot[1] = '-' + aligned_rot[1]
                
                # Take degrees w.r.t plausible range.
                for u in range(len(aligned_rot)):
                    aligned_rot[u] = str((float(aligned_rot[u]) + 180)%360 - 180)
                # for u in range(len(aligned_rot)):
                #     if aligned_rot[u][0] == '-':
                #         aligned_rot[u] = aligned_rot[u][1:]
                #     else:
                #         aligned_rot[u] = '-' + aligned_rot[u]

                tar_frame[k:k+3] = aligned_rot

            

        # change the array with the new values
        target_bvh[j] = ' '.join(tar_frame)
    




    # Once all the frame have been processed, write the output.
    f = open(output_dir, 'w')
    f.writelines(target_bvh)
    f.close()



if __name__ == '__main__':
    transfer_rot('data/simple_kick.bvh', 'data/punch_mxm.bvh', 'data/output.bvh')