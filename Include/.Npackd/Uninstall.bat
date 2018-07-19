msiexec.exe /qn /norestart /Lime .Npackd\UninstallMSI.log /x{61246987-8d99-44a9-8ff5-e2e3f503b72d}
set err=%errorlevel%
type .Npackd\UninstallMSI.log
rem 3010=restart required
if %err% equ 3010 exit 0
rem 1605=unknown product
if %err% equ 1605 exit 0
if %err% neq 0 exit %err%
