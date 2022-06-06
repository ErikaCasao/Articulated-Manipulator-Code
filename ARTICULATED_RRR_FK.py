import numpy as np
import math
import PySimpleGUI as sg
import pandas as pd

# GUI code

sg.theme('BrightColors')

# Excel read code

EXCEL_FILE = 'ARTICULATED_RRR_FK.xlsx'
df= pd.read_excel(EXCEL_FILE)

# Lay-out code

Main_layout=[
        [sg.Push(), sg.Text('ARTICULATED RRR MEXE CALCULATOR', font = ("BankGothic Md BT", 20)), sg.Push()],
        [sg.Push(),sg.Text('   ', font = ("Lucida Sans Typewriter", 10)),sg.Push()],
        [sg.Text('Forward Kinematics Calculator', font = ("Lucida Sans Typewriter", 14))],
        [sg.Text('Fill out the following fields:',font = ("Lucida Sans Typewriter", 10))],
        [sg.Push(),sg.Text('   ', font = ("Lucida Sans Typewriter", 5)),sg.Push()],
        [sg.Push(),sg.Text('a1 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='a1', size=(10,10)),
         sg.Text('a2 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='a2', size=(10,10)),
         sg.Text('a3 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='a3', size=(10,10)),
         sg.Text('T1 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='T1', size=(10,10)),
         sg.Text('T2 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='T2', size=(10,10)),
         sg.Text('T3 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='T3', size=(10,10)),sg.Push()],
        [sg.Push(),sg.Text('   ', font = ("Lucida Sans Typewriter", 5)),sg.Push()],
        [sg.Push(),sg.Button('Click this before Solving Forward Kinematics', font = ("Lucida Sans Typewriter", 13), size=(40,2), button_color=('black', 'seagreen2')), sg.Push(),
         sg.Push(),sg.Text('OR ', font = ("Lucida Sans Typewriter", 13)),sg.Push(),
         sg.Push(),sg.Button('Solve Inverse Kinematics', font = ("Lucida Sans Typewriter", 13), size=(40,2), button_color=('black', 'cyan')), sg.Push()],
        [sg.Push(),sg.Button('Solve Forward Kinematics', disabled=True, tooltip = 'Go first to "Click this before Solving Forward Kinematics!"', font = ("Lucida Sans Typewriter", 13), size=(40,0),button_color=('white', 'purple2')), sg.Push(),
         sg.Push(),sg.Text('    ', font = ("Lucida Sans Typewriter", 13)),sg.Push(),
         sg.Push(),sg.Button('Jacobian Matrix (J)',disabled=True, font = ("Lucida Sans Typewriter", 10), size=(13,2), button_color=('white', 'black')),
         sg.Button('Det(J)', disabled=True, font = ("Lucida Sans Typewriter", 10), size=(10,2), button_color=('white', 'black')), 
         sg.Button('Inverse of J', disabled=True,  font = ("Lucida Sans Typewriter", 10), size=(12,2), button_color=('white', 'black')),
         sg.Button('Transpose of J', disabled=True,  font = ("Lucida Sans Typewriter", 10), size=(13,2), button_color=('white', 'black')), sg.Push()],
         
        [sg.Push(),sg.Frame('Position Vector:',[[
             sg.Text('X =' , font = ("Lucida Sans Typewriter", 10)),sg.InputText(key='X', size=(13,2)),
             sg.Text('Y =' , font = ("Lucida Sans Typewriter", 10)),sg.InputText(key='Y', size=(14,2)),
             sg.Text('Z =' , font = ("Lucida Sans Typewriter", 10)),sg.InputText(key='Z', size=(13,2))]]), sg.Push(),
             sg.Push(),sg.Text('    ', font = ("Lucida Sans Typewriter", 13)),sg.Push(),
             sg.Push(), sg.Button('Path and Trajectory Planning',disabled=True, font = ("Lucida Sans Typewriter", 10), size=(52,2), button_color=('black', 'spring green')), sg.Push()
        ],
        [sg.Push(), sg.Frame('H0_3 Transformation Matrix = ',[[sg.Output(size=(53,12))]]),sg.Push(),
         sg.Push(),sg.Text('    ', font = ("Lucida Sans Typewriter", 13)),sg.Push(),
         sg.Push(),sg.Image('ARTICULATED_PICTURE.gif'), sg.Push()],
        [sg.Push(),sg.Submit(font = ("Courier New", 10)),sg.Exit(font = ("Courier New", 10)),sg.Push()]
       
       ]
#Window Code
window = sg.Window('ARTICULATED RRR MEXE CALCULATOR', Main_layout, resizable= True)

#Inverse Kinematics Window Function

def Inverse_Kinematics_Window():
    sg.theme('brightcolors')
    EXCEL_FILE= 'ARTICULATED_RRR_IK.xlsx'
    IK_df = pd.read_excel(EXCEL_FILE)
    
    
    IK_Layout = [
        [sg.Push(), sg.Text('Inverse Kinematics', font = ("BankGothic Md BT", 20)), sg.Push()],
        [sg.Text('Fill out the following fields:',font = ("Lucida Sans Typewriter", 10))],
        [sg.Text('a1 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='a1', size=(8,10)),
         sg.Text('cm', font = ("Lucida Sans Typewriter", 10)),
         sg.Text('X = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='X', size=(8,10)),
         sg.Text('cm', font = ("Lucida Sans Typewriter", 10))],
          
        [sg.Text('a2 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='a2', size=(8,10)),
         sg.Text('cm', font = ("Lucida Sans Typewriter", 10)),
         sg.Text('Y = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='Y', size=(8,10)),
         sg.Text('cm', font = ("Lucida Sans Typewriter", 10))],
           
        [sg.Text('a3 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='a3', size=(8,10)),
         sg.Text('cm', font = ("Lucida Sans Typewriter", 10)),
         sg.Text('Z = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText('0', key='Z', size=(8,10)),
         sg.Text('cm', font = ("Lucida Sans Typewriter", 10))],
            
        [sg.Button('Solve Inverse Kinematics', font = ("Lucida Sans Typewriter", 12), button_color=('black', 'cyan')), sg.Push()], 
            
        [sg.Frame('Position Vector:',[[
        sg.Text('Th1 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText(key='IK_Th1', size=(10,10)),
        sg.Text('degrees', font = ("Lucida Sans Typewriter", 10)),
                 
        sg.Text('Th2 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText(key='IK_Th2', size=(10,10)),
        sg.Text('degrees', font = ("Lucida Sans Typewriter", 10)),
                 
        sg.Text('Th3 = ', font = ("Lucida Sans Typewriter", 10)),sg.InputText(key='IK_Th3', size=(10,10)),
        sg.Text('degrees', font = ("Lucida Sans Typewriter", 10)),]])],
           
        [sg.Push(), sg.Submit(font = ("Courier New", 10)),sg.Exit(font = ("Courier New", 10)),sg.Push()]
]    
        
    # Window Code
    Inverse_Kinematics_window = sg.Window('Inverse Kinematics', IK_Layout)
    
    while True:
        event, values = Inverse_Kinematics_window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        elif event == 'Solve Inverse Kinematics':
            
            # Link Lengths
            a1 = float(values['a1'])
            a2 = float(values['a2'])
            a3 = float(values['a3'])
            # Position Vectors
            X0_3 = float(values['X'])
            Y0_3 = float(values['Y'])
            Z0_3 = float(values['Z'])
            
            try:
                Th1 = np.degrees(np.arctan(Y0_3/X0_3))
            except:
                Th1 = -1 #NAN
                sg.popup('Warning! The values entered are not valid.')
                sg.popup('Restart the GUI and enter the proper values.')
                break            
           
            Th1 = np.degrees(np.arctan(Y0_3/X0_3))
            r1 = Z0_3 - a1
            r2 = math.sqrt((Y0_3**2)+(X0_3**2))
            r3 = math.sqrt((r1**2)+(r2**2))
            
            try:
                phi1 = np.arccos((a3**2-a2**2-r3**2)/(-(2.0)*a2*r3))*180.0/np.pi
            except:
                phi1 = -1 #NAN
                sg.popup('Warning! The values entered are not valid.')
                sg.popup('Restart the GUI and enter the proper values.')
                break
            
            phi1 = np.arccos((a3**2-a2**2-r3**2)/(-(2.0)*a2*r3))*180.0/np.pi
            phi2 = np.arccos((r3**2-a2**2-a3**2)/(-(2.0)*a2*a3))*180.0/np.pi
            phi3 = np.degrees(np.arctan(r1/r2))
            Th2 = (phi3)-(phi1)
            
            Th3 = 180 - phi2

            #print("Th1 = ", np.around(Th1,3))
            #print(Th1)
            #print("Th2 = ", np.around(Th2,3))
            #print(Th2)
            #print("Th3 = ", np.around(Th3,3))
            
            Th1 = Inverse_Kinematics_window['IK_Th1'].Update(np.around(Th1,3))
            Th2 = Inverse_Kinematics_window['IK_Th2'].Update(np.around(Th2,3))
            Th3 = Inverse_Kinematics_window['IK_Th3'].Update(np.around(Th3,3))
            
        elif event == 'Submit':
            IK_df = IK_df.append(values, ignore_index=True)
            IK_df.to_excel(EXCEL_FILE, index=False)
            sg.popup("Data Saved Successfully!")
    Inverse_Kinematics_window.close()
                
            

# Variable Codes for disabling buttons
disable_FK = window['Solve Forward Kinematics']
disable_J = window['Jacobian Matrix (J)']
disable_DetJ = window['Det(J)']
disable_IV = window['Inverse of J']
disable_TJ = window['Transpose of J']
disable_PT = window['Path and Trajectory Planning']

def clear_input():
    for key in values:
        window[key]('')
    return None

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    
    if event == 'CLICK THIS FIRST TO START SOLVING!':
        disable_FK.update(disabled=False)
        disable_J.update(disabled=True)
        disable_DetJ.update(disabled=True)
        disable_IV.update(disabled=True)
        disable_TJ.update(disabled=True)
        disable_PT.update(disabled=True)

    if event == 'Solve Forward Kinematics':
        # Forward Kinematic Codes
        # Link Lengths in cm
        a1 = values['a1']
        a2 = values['a2']
        a3 = values['a3']
        # Joint Variables in degrees
        T1 = values['T1']
        T2 = values['T2']
        T3 = values['T3']
        # Joint Variables in radians
        T1 = (float(T1)/180.0)*np.pi
        T2 = (float(T2)/180.0)*np.pi
        T3 = (float(T3)/180.0)*np.pi
        # If Joint Variable are ds don't need to convert
        ## D-H Parameter Table (This is the only part you need to edit for every new mechanical manipulator.)
        # Rows = no. of HTM, Columns - no. of Parameters
        # Theta, alpha, r, d
        DHPT = [[(0.0/180.0)*np.pi+float(T1),(90.0/180.0)*np.pi,0,float(a1)],
                [(0.0/180.0)*np.pi+float(T2),(0.0/180)*np.pi,float(a2),0],
                [(0.0/180.0)*np.pi+float(T3),(0.0/180)*np.pi,float(a3),0]]    
        
        i = 0
        H0_1 = [[np.cos(DHPT[i][0]),-np.sin(DHPT[i][0])*np.cos(DHPT[i][1]),np.sin(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.cos(DHPT[i][0])],
                [np.sin(DHPT[i][0]),np.cos(DHPT[i][0])*np.cos(DHPT[i][1]),-np.cos(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.sin(DHPT[i][0])],
                [0,np.sin(DHPT[i][1]),np.cos(DHPT[i][1]),DHPT[i][3]],
                [0,0,0,1]]
        i = 1
        H1_2 = [[np.cos(DHPT[i][0]),-np.sin(DHPT[i][0])*np.cos(DHPT[i][1]),np.sin(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.cos(DHPT[i][0])],
                [np.sin(DHPT[i][0]),np.cos(DHPT[i][0])*np.cos(DHPT[i][1]),-np.cos(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.sin(DHPT[i][0])],
                [0,np.sin(DHPT[i][1]),np.cos(DHPT[i][1]),DHPT[i][3]],
                [0,0,0,1]]
        i = 2
        H2_3 = [[np.cos(DHPT[i][0]),-np.sin(DHPT[i][0])*np.cos(DHPT[i][1]),np.sin(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.cos(DHPT[i][0])],
                [np.sin(DHPT[i][0]),np.cos(DHPT[i][0])*np.cos(DHPT[i][1]),-np.cos(DHPT[i][0])*np.sin(DHPT[i][1]),DHPT[i][2]*np.sin(DHPT[i][0])],
                [0,np.sin(DHPT[i][1]),np.cos(DHPT[i][1]),DHPT[i][3]],
                [0,0,0,1]]           
                    
        H0_1 = np.matrix(H0_1)
        #print("H0_1=")
        #print(H0_1)

        H1_2 = np.matrix(H1_2)
        #print("H1_2=")
        #print(H1_2)

        H2_3 = np.matrix(H2_3)
        #print("H2_3=")
        #print(H2_3)

        H0_2 = np.dot(H0_1,H1_2)
        H0_3 = np.dot(H0_2,H2_3)
        print("H0_3=")
        print(np.matrix(H0_3))

        # Position Vectors X Y Z
        X0_3 = H0_3[0,3]
        print("X = ")
        print(X0_3)                   
        
        Y0_3 = H0_3[1,3]
        print("Y = ")
        print(Y0_3)

        Z0_3 = H0_3[2,3]
        print("Z = ")
        print(Z0_3)

        
        disable_J.update(disabled=False)
        disable_PT.update(disabled=False)
        
    if event == 'Submit':
        df = df.append(values, ignore_index=True)
        df.to_excel(EXCEL_FILE, index=False)
        sg.popup('Data Saved Successfully!')            
            
    if event == 'Jacobian Matrix (J)':
        ### Jacobian Matrix
        ## 1. Linear/Prismatic Vectors
        Z_1 = [[0],[0],[1]]

        # Rows 1-3, Column 1
        J1a = [[1,0,0],[0,1,0],[0,0,1]]
        J1a = np.dot(J1a,Z_1)

        try:
            H0_3 = np.matrix(H0_3)
        except:
            H0_3 = -1 #NAN
            sg.popup('Warning!')
            sg.popup('Restart the GUI then go first to "Click this before Solving Forward Kinematics!"')
            break

        J1b_1 = H0_3[0:3,3:] 
        #print("J1b_1 = ")
        #print(np.matrix(J1b_1)
        
        J1b_2 = [[0],[0],[0]]
        #print(np.matrix(J1b_2))
        
        J1b = J1b_1 - J1b_2
        #print('J1b = ')
        #print(np.matrix(J1b))

        J1 = [[(J1a[1,0]*J1b[2,0])-(J1a[2,0]*J1b[1,0])],
              [(J1a[2,0]*J1b[0,0])-(J1a[0,0]*J1b[2,0])],
              [(J1a[0,0]*J1b[1,0])-(J1a[1,0]*J1b[0,0])]]
        #print('J1 = ')
        #print(np.matrix(J1))

        # Rows 1-3, Column 2
        try:
            H0_1 = np.matrix(H0_1)
        except:
            H0_1 = -1 #NAN
            sg.popup('Warning!')
            sg.popup('Restart the GUI then go first to "Click this before Solving Forward Kinematics!"')
            break
                    
        J2a = H0_1[0:3,0:3]
        J2a = np.dot(J2a,Z_1)
        #print("J2a = ")
        #print(J2a)

        J2b_1 = H0_3[0:3,3:]
        J2b_1 = np.matrix(J2b_1)
        #print("J2b_1 = ")
        #print(J2b_1)

        J2b_2 = H0_1[0:3,3:]
        J2b_2 = np.matrix(J2b_2)
        #print("J2b_2 = ")
        #print(J2b_2)

        J2b = J2b_1 - J2b_2
        #print("J2b = ")
        #print(J2b)

        J2 = [[(J2a[1,0]*J2b[2,0])-(J2a[2,0]*J2b[1,0])],
              [(J2a[2,0]*J2b[0,0])-(J2a[0,0]*J2b[2,0])],
              [(J2a[0,0]*J2b[1,0])-(J2a[1,0]*J2b[0,0])]]
        #print("J2 = ")
        #print(np.matrix(J2))
        
        # Rows 1-3, Column 3
        J3a = H0_2[0:3,0:3]
        J3a = np.dot(J3a,Z_1)
        #print("J3a = ")
        #print(J3a)

        J3b_1 = H0_3[0:3,3:]
        J3b_1 = np.matrix(J3b_1)
        #print("J3b_1 = ")
        #print(J3b_1)

        J3b_2 = H0_2[0:3,3:]
        J3b_2 = np.matrix(J3b_2)
        #print("J3b_2 = ")
        #print(J3b_2)

        J3b = J3b_1 - J3b_2
        #print("J3b = ")
        #print(J3b)
        J3 = [[(J3a[1,0]*J3b[2,0])-(J3a[2,0]*J3b[1,0])],
              [(J3a[2,0]*J3b[0,0])-(J3a[0,0]*J3b[2,0])],
              [(J3a[0,0]*J3b[1,0])-(J3a[1,0]*J3b[0,0])]]
        #print("J3 = ")
        #print(np.matrix(J3))
        J3 = [[(J3a[1,0]*J3b[2,0])-(J3a[2,0]*J3b[1,0])],
              [(J3a[2,0]*J3b[0,0])-(J3a[0,0]*J3b[2,0])],
              [(J3a[0,0]*J3b[1,0])-(J3a[1,0]*J3b[0,0])]
             ]
        #print("J3 = ")
        #print(np.matrix(J3))

        ## 2. Rotation/Orientation Vectors
        J4 = [[0],[0],[1]]
        J4 = np.matrix(J4)
        #print("J4 = ")
        #print(J4)

        J5 = H0_1[0:3,0:3]
        J5 = np.dot(J5,Z_1)
        J5 = np.matrix(J5)
        #print("J5 = ")
        #print(J5)
         
        J6 = H0_2[0:3,0:3]
        J6 = np.dot(J6,Z_1)
        J6 = np.matrix(J6)
        #print("J6 = ")
        #print(J6)
            
        ## 3. Concatenated Jacobian Matrix
        JM1 = np.concatenate((J1,J2,J3),1)
        JM2 = np.concatenate((J4,J5,J6),1)

        JCM = np.concatenate((JM1,JM2),0)
        #print("JACOBIAN MATRIX = ")
        #print(JCM)
        
        sg.popup('J = ', JCM)        

        DJ = np.linalg.det(JM1)
        if DJ == 0.0 or DJ == -0.0:
            disable_IV.update(disabled=True)
            sg.popup('Warning: Jacobian Matrix is Non-Invertible!')
        
        elif DJ !=0.0 or DJ != 0.0:
            disable_IV.update(disabled=False)
        
        
        disable_J.update(disabled=True)
        disable_DetJ.update(disabled=False)
        disable_TJ.update(disabled=False)

    if event == 'Det(J)':
        # singularity = Det(J)
        # np.linalg.det(M)
        # Let JM1 become the 3x3 position matrix for obtaining the determinant
        
        try:
            JM1 = np.concatenate((J1,J2,J3),1)
        except:
            JM1 = -1 #NAN
            sg.popup('Warning!')
            sg.popup('Restart the GUI then go first to "Click this before Solving Forward Kinematics!"')
            break
            
        DJ = np.linalg.det(JM1)
        #print('Determinant of J = ', DJ)
        sg.popup('Determinant of J = ', DJ)
        
        if DJ == 0.0 or DJ == -0.0:
            disable_IV.update(disabled=True)
            sg.popup('Warning: Jacobian Matrix is Non-Invertible!')
   
    if event == 'Inverse of J':
        # Inv(J)
        
        try:
            JM1 = np.concatenate((J1,J2,J3),1)
        except:
            JM1 = -1 #NAN
            sg.popup('Warning!')
            sg.popup('Restart the GUI then go first to "Click this before Solving Forward Kinematics!"')
            break
            
        IJ = np.linalg.inv(JM1)
        #print('Inverse Jacobian = ', IJ)
        sg.popup('Inverse Jacobian Matrix', np.around(IJ,3))

    if event == 'Transpose of J':
        # Transpose of Jacobian Matrix
        try:
            JM1 = np.concatenate((J1,J2,J3),1)
        except:
            JM1 = -1 #NAN
            sg.popup('Warning!')
            sg.popup('Restart the GUI then go first to "Click this before Solving Forward Kinematics!"')
            break
            
        TJ = np.transpose(JM1)
        #print('Transpose = ', TJ)
        sg.popup('Transpose of Jacobian Matrix = ', TJ)
        
    elif event == 'Solve Inverse Kinematics':
        
        Inverse_Kinematics_Window()               
    
        
window.close()




