from glob import glob
import os
import shutil
import subprocess

UPLOAD_LOCATION = 'RunPDF/'
files = glob(UPLOAD_LOCATION + '*.pdf')
file_result_folder = files[0].split('/')[1].split('.')[0]

# make the ResultFolder
location = os.path.join('ResultToDownload', file_result_folder)
os.makedirs(location)
print(f"Folder '{location}' created successfully.")

# AppEncoder
script_path = "AppEncoder.py"
try:
    subprocess.run(["python", script_path], check=True)
    print(f"Successfully ran '{script_path}'.")
    print('-----Stage 1 pass-----\nget the token file! Stage 1 pass')
except subprocess.CalledProcessError as e:
    print(f"Error running '{script_path}': {e}")
    
# AppAnalyzer
script_path = "AppAnalyzer.py"
try:
    subprocess.run(["python", script_path], check=True)
    print(f"Successfully ran '{script_path}'.")
    print('-----Stage 2 pass-----\nGPU computing done! Stage 2 pass')
except subprocess.CalledProcessError as e:
    print(f"Error running '{script_path}': {e}")

# AppIllustrator
script_path = "AppIllustrator.py"
try:
    subprocess.run(["python", script_path], check=True)
    print(f"Successfully ran '{script_path}'.")
    print('-----Stage 3 pass-----\nTendency figure done! Stage 3 pass')
except subprocess.CalledProcessError as e:
    print(f"Error running '{script_path}': {e}")
    
# AppReportColored
script_path = "AppReportColored.py"
try:
    subprocess.run(["python", script_path], check=True)
    print(f"Successfully ran '{script_path}'.")
    print('-----Stage 4 pass-----\nReport done! Stage 4 pass')
except subprocess.CalledProcessError as e:
    print(f"Error running '{script_path}': {e}")

# Move the data
## report
PDF_name = files[0].split('/')[1]
shutil.move(files[0], os.path.join(location, PDF_name))
## 'TempPDF/total_txt.joblib'
shutil.move('TempPDF/total_txt.joblib', os.path.join(location, 'total_txt.joblib'))
## 'ix.joblib'
shutil.move('TempPDF/i0.joblib', os.path.join(location, 'i0.joblib'))
shutil.move('TempPDF/i1.joblib', os.path.join(location, 'i1.joblib'))
shutil.move('TempPDF/i2.joblib', os.path.join(location, 'i2.joblib'))
shutil.move('TempPDF/i3.joblib', os.path.join(location, 'i3.joblib'))
shutil.move('TempPDF/i4.joblib', os.path.join(location, 'i4.joblib'))
shutil.move('TempPDF/i5.joblib', os.path.join(location, 'i5.joblib'))
shutil.move('TempPDF/i6.joblib', os.path.join(location, 'i6.joblib'))
shutil.move('TempPDF/i7.joblib', os.path.join(location, 'i7.joblib'))
shutil.move('TempPDF/i8.joblib', os.path.join(location, 'i8.joblib'))
shutil.move('TempPDF/i9.joblib', os.path.join(location, 'i9.joblib'))
shutil.move('TempPDF/i10.joblib', os.path.join(location, 'i10.joblib'))
shutil.move('TempPDF/i11.joblib', os.path.join(location, 'i11.joblib'))
shutil.move('TempPDF/i12.joblib', os.path.join(location, 'i12.joblib'))
shutil.move('TempPDF/AllIndex.joblib', os.path.join(location, 'AllIndex.joblib'))
## "Results/Tendency.jpg"
shutil.move("Results/Tendency.jpg", os.path.join(location, 'Tendency.jpg'))
## report
shutil.move("Results/Community.html", os.path.join(location, 'Community.html'))
shutil.move("Results/Air_Pollution.html", os.path.join(location, 'Air_Pollution.html'))
shutil.move("Results/Greenhouse_Gas.html", os.path.join(location, 'Greenhouse_Gas.html'))
shutil.move("Results/Water_Consumption.html", os.path.join(location, 'Water_Consumption.html'))
shutil.move("Results/Mining_Consumption.html", os.path.join(location, 'Mining_Consumption.html'))
shutil.move("Results/Work_Environment.html", os.path.join(location, 'Work_Environment.html'))
shutil.move("Results/Safety_Health.html", os.path.join(location, 'Safety_Health.html'))
shutil.move("Results/Human_Right.html", os.path.join(location, 'Human_Right.html'))
shutil.move("Results/Governance_Risk.html", os.path.join(location, 'Governance_Risk.html'))
shutil.move("Results/Production_Cost.html", os.path.join(location, 'Production_Cost.html'))
shutil.move("Results/Domestic_Job.html", os.path.join(location, 'Domestic_Job.html'))
shutil.move("Results/Economic_Ripple.html", os.path.join(location, 'Economic_Ripple.html'))
shutil.move("Results/Domestic_Reflux.html", os.path.join(location, 'Domestic_Reflux.html'))
print(f'-----Stage 5 pass-----\n go to {location} find everything')


