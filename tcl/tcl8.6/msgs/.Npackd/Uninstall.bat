msiexec.exe /qn /norestart /Lime .Npackd\UninstallMSI.log /x{a2fc01e0-059e-4d21-afd2-b63a7e1ef3cd}
set err=%errorlevel%
type .Npackd\UninstallMSI.log
rem 3010=restart required
if %err% equ 3010 exit 0
rem 1605=unknown product
if %err% equ 1605 exit 0
if %err% neq 0 exit %err%
