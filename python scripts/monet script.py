import sys
import clr #pip install pythonnet NOT clr

# define path to the Mo.net Linked DLL and add this to system path

assembly_path = r"C:\GitHub\OAC\LinkedFundsForPython\Mo.net Project\LinkedFundsForPython\Linked_DLLFolder"
sys.path.append(assembly_path)

# add Mo.net kernel assembly references to the CLR

clr.AddReference("Sal.CalculationEngine.GenCore")
clr.AddReference("Sal.CalculationEngine.Interfaces.Entities")

# add Mo.net projection DLL reference to the CLR

clr_ref = clr.AddReference("Linked_Monet")
monet_type = clr_ref.GetType('Monet')

# invoke Mo.net interface methods

initCmdLine_method = monet_type.GetMethod('InitCommandLine')
initCmdLine_method.Invoke(None, [None])

init_method = monet_type.GetMethod('Initialise')
init_method.Invoke(None, [True])

initProj_method = monet_type.GetMethod('InitialiseProjections')
initProj_method.Invoke(None, [])

# obtain a list of the projections inside the DLL

projections = monet_type.GetProperty('Projections')

# create a reference to the Linked projection task

linkedproj = projections.GetValue(None).Linked

# uncomment the next line to override the SterlInt parameter associated with the
# Linked projection

# linkedproj.SterlInt = 0.1

# run the projection

linkedproj.Run()

# show the sterling result at time=0 

print()
print(f'SterlInt = {linkedproj.SterlInt}')
print(f'SterlRes(0) = {linkedproj.SterlRes(0)}')