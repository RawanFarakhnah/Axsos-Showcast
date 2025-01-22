#Selection Sort
#Refrence Video
#https://vimeo.com/95669275?turnstile=0.aeVeVJtaS-LDzQ8mYj--GqAWGsjCn-_At_Ij99nUxWqBd-Ga93zHYUnX6JSnpAMI3dM4mcRZx40LV5Zxg2iDaOqmGaYg-rvzAs5iDyPT86Mm6IisaJXYAi_w6xAoNdCUY1F3-YwfFsKJ3S49uOlg-gifyt8R_lOmViDynCVDgztw4f7t_Ztx-jYt4KjQy57cCfHHLWNlOBLoofsX1BIhz9FTQW2A6mce-YJJCVcuZMCdobhT8C3d1PiJQELFJvjUWObVMvf6r32YUirleC8Rd16vLfXmEsIm1w4x9M5vMZWxbxPLZmlfSqPAm2SQivS-hRYGjPekMU-dmubt9vK7P4LlYlFkCdNbvvwy9FNAl1oRnD2cmurby9N-XFyup4CkmMJxwyklaJLMiqCLQEARmFJ0DEPcuzsfsbzU54HhjDQFDsbSYCov9O929f_WLMEpY_qeMIvkQ4W7I8JtDKt0Yzh9yC7G4TCukoASqwIzWIura5Rm_NWYEVCVz0MvxIuI8nmbxnztQ4GZ60XiseCK4iHzXXI-1voVHd8hrRc5jcNg4g3X4Q_CZ_EiC4uVLVmxPg0i6H6r67_RUrDdyt-St6O_r0VDtv0jg0Vv8c0QLrYG485CXLtoMKaKiKgf8-_tyHlYy5r_9RmEg2OYsJn_eyJB6WViLLW9Try5LeWWS6YWHrkULadaItIS_qAaVLcWwCKPCiHn9vJODKCfSQY0mivY92GYskUREskmNWcsED_7mi8lSmEW_VF8GXxZCHwdRModrDVNpsX1R07Wx5dT7v9cuMQSkmQfn3G5TIoNFVo.5hcs671OipysNd9SEX6VMw.1c1ceac28fa5d7b0a35a5ff2be025bde594439f1065306bf4f2a8f4fe2c8ffca

#assuming minimum value is first element position 
#search rest of this element if there any element is smoller
#than current element if yes we have to switch it
#other waise it consider this position is sorted and we will 
#contine the same steps begin from next position
#{I surely no all small element was placed behind the next position}



myList = [3, 1, 5, 6, 7, 4, 8]

def selection_sort(any_list):
    length = len(any_list)
    for p1 in range(length):
        min_index = p1
        for p2 in range(p1 + 1, length):
            if any_list[p2] < any_list[min_index]:
                min_index = p2
              
        any_list[p1], any_list[min_index] =  any_list[min_index], any_list[p1]  
    return any_list

print("\nUsing Selecton Sort")
print("Original List:", myList)
print("Sorted List:", selection_sort(myList))


