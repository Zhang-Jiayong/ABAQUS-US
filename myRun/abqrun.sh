

### ********** abaqus path ********** 
export abaqus_root=/home/zhangjiayong/opt/DassaultSystemes/Abaqus2019
export PATH=${abaqus_root}/SIMULIA/Commands:$PATH



### ********** server setting ********** 
### - check port usage
netstat -tulpn | grep LISTEN 
# check 27800
# kill  xxxx

### - start license server
export serverPATH=$HOME/opt/DassaultSystemes/SolidSQUAD_License_Servers
export LM_LICENSE_FILE=${serverPATH}/Licenses/lmgrd_SSQ.lic
${serverPATH}/Bin/lmgrd

### - check license status
${abaqus_root}/SIMULIA/Commands/abaqus licensing ru



### ********** start abaqus **********
### - umat example
${abaqus_root}/SIMULIA/Commands/abaqus job=UNIUSER_CLA_KIN user=UMAT_PCLK

### - viewer 
# -mesa : error regarding OpenGL
#
${abaqus_root}/SIMULIA/Commands/abaqus cae  -mesa
${abaqus_root}/SIMULIA/Commands/abaqus view -mesa



