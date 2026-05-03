# MuMu Emulator Python API

This project is maintained by DreamStudio Research.

- [MuMu Emulator Python API](#mumu-emulator-python-api)
    - [Project Overview](#project-overview)
    - [How to Use](#how-to-use)
        - [Setting the MuMuManager Path](#setting-the-mumumanager-path)
        - [Emulator Index Explained](#emulator-index-explained)
        - [Selecting an Emulator](#selecting-an-emulator)
        - [An Example](#an-example)
        - [Note](#note)
    - [API Classes](#api-classes)
        - [Driver class (driver)](#driver-class-driver)
            - [Network bridge driver (bridge)](#network-bridge-driver-bridge)
                - [Install the bridge driver (install)](#install-the-bridge-driver-install)
                - [Uninstall the bridge driver (uninstall)](#uninstall-the-bridge-driver-uninstall)
        - [Permission class (permission)](#permission-class-permission)
            - [\* ROOT permission (root)](#-root-permission-root)
                - [Enable ROOT permission (enable)](#enable-root-permission-enable)
                - [Disable ROOT permission (disable)](#disable-root-permission-disable)
        - [Power class (power)](#power-class-power)
            - [Start the emulator (start)](#start-the-emulator-start)
            - [Shut down the emulator (shutdown|stop)](#shut-down-the-emulator-shutdownstop)
            - [Restart the emulator (restart|reboot)](#restart-the-emulator-restartreboot)
        - [Window class (window)](#window-class-window)
            - [Show window (show)](#show-window-show)
            - [Hide window (hidden)](#hide-window-hidden)
            - [Adjust window size or position (layout)](#adjust-window-size-or-position-layout)
        - [App class (app)](#app-class-app)
            - [Install an app (install)](#install-an-app-install)
            - [Uninstall an app (uninstall)](#uninstall-an-app-uninstall)
            - [Launch an app inside the emulator (launch)](#launch-an-app-inside-the-emulator-launch)
            - [Close an app inside the emulator (close)](#close-an-app-inside-the-emulator-close)
            - [\* Check whether an app exists (exists)](#-check-whether-an-app-exists-exists)
            - [\* Check whether an app does not exist (doesntExists)](#-check-whether-an-app-does-not-exist-doesntexists)
            - [Get the list of installed apps (get\_installed)](#get-the-list-of-installed-apps-get_installed)
            - [\* Get app state (state)](#-get-app-state-state)
        - [Core class (core)](#core-class-core)
            - [Create an emulator (create)](#create-an-emulator-create)
            - [Clone an emulator (clone)](#clone-an-emulator-clone)
            - [Delete an emulator (delete)](#delete-an-emulator-delete)
            - [Rename an emulator (rename)](#rename-an-emulator-rename)
            - [Back up an emulator (export)](#back-up-an-emulator-export)
            - [Import an emulator (import\_)](#import-an-emulator-import_)
            - [Limit CPU usage (limit\_cpu)](#limit-cpu-usage-limit_cpu)
        - [Android event class (androidEvent)](#android-event-class-androidevent)
            - [Rotate screen (rotate)](#rotate-screen-rotate)
            - [Go to home screen (go\_home)](#go-to-home-screen-go_home)
            - [Back (back)](#back-back)
            - [Pin window on top (top\_most)](#pin-window-on-top-top_most)
            - [Fullscreen window (fullscreen)](#fullscreen-window-fullscreen)
            - [Shake (shake)](#shake-shake)
            - [Screenshot (screenshot)](#screenshot-screenshot)
            - [Volume up (volume\_up)](#volume-up-volume_up)
            - [Volume down (volume\_down)](#volume-down-volume_down)
            - [Volume mute (volume\_mute)](#volume-mute-volume_mute)
            - [Task key (go\_task)](#task-key-go_task)
            - [Set virtual location (location)](#set-virtual-location-location)
            - [Set gyro sensor (gyro)](#set-gyro-sensor-gyro)
        - [Shortcut class (shortcut)](#shortcut-class-shortcut)
            - [Create a desktop shortcut (create)](#create-a-desktop-shortcut-create)
            - [Delete a desktop shortcut (delete)](#delete-a-desktop-shortcut-delete)
        - [Simulation class (simulation)](#simulation-class-simulation)
            - [Set MAC address (mac\_address)](#set-mac-address-mac_address)
            - [Set IMEI (imei)](#set-imei-imei)
            - [Set IMSI (imsi)](#set-imsi-imsi)
            - [Set Android ID (android\_id)](#set-android-id-android_id)
            - [Set device model (model)](#set-device-model-model)
            - [Set motherboard brand (brand)](#set-motherboard-brand-brand)
            - [Set hardware manufacturer (solution)](#set-hardware-manufacturer-solution)
            - [Set phone number (phone\_number)](#set-phone-number-phone_number)
            - [Set GPU model (gpu\_model)](#set-gpu-model-gpu_model)
        - [Setting class (setting)](#setting-class-setting)
            - [Get all configuration items (all)](#get-all-configuration-items-all)
            - [Get one or more configuration items (get)](#get-one-or-more-configuration-items-get)
            - [Set one or more configuration items (set)](#set-one-or-more-configuration-items-set)
            - [Set configuration from a JSON file (set\_by\_json)](#set-configuration-from-a-json-file-set_by_json)
            - [\* Check whether a config equals a value (equal)](#-check-whether-a-config-equals-a-value-equal)
            - [\* Check whether a config does not equal a value (not\_equal)](#-check-whether-a-config-does-not-equal-a-value-not_equal)
            - [\* If a config equals a value, change it to another value (equal\_then\_set)](#-if-a-config-equals-a-value-change-it-to-another-value-equal_then_set)
            - [\* If a config does not equal a value, change it to another value (not\_equal\_then\_set)](#-if-a-config-does-not-equal-a-value-change-it-to-another-value-not_equal_then_set)
        - [\* Screen class (screen)](#-screen-class-screen)
            - [Set emulator resolution (resolution)](#set-emulator-resolution-resolution)
            - [Set to phone resolution (resolution\_mobile)](#set-to-phone-resolution-resolution_mobile)
            - [Set to tablet resolution (resolution\_tablet)](#set-to-tablet-resolution-resolution_tablet)
            - [Set to ultrawide resolution (resolution\_ultrawide)](#set-to-ultrawide-resolution-resolution_ultrawide)
            - [Set emulator DPI (dpi)](#set-emulator-dpi-dpi)
            - [Set emulator brightness (brightness)](#set-emulator-brightness-brightness)
            - [Set max frame rate (max\_frame\_rate)](#set-max-frame-rate-max_frame_rate)
            - [Set dynamic frame rate adjustment (dynamic\_adjust\_frame\_rate)](#set-dynamic-frame-rate-adjustment-dynamic_adjust_frame_rate)
            - [Set vertical sync (vertical\_sync)](#set-vertical-sync-vertical_sync)
            - [Show frame rate (show\_frame\_rate)](#show-frame-rate-show_frame_rate)
            - [Auto-rotate window (window\_auto\_rotate)](#auto-rotate-window-window_auto_rotate)
        - [Performance class (performance)](#performance-class-performance)
            - [Set CPU and memory (set)](#set-cpu-and-memory-set)
            - [Set CPU count (cpu)](#set-cpu-count-cpu)
            - [Set memory size (memory)](#set-memory-size-memory)
            - [Force discrete graphics (force\_discrete\_graphics)](#force-discrete-graphics-force_discrete_graphics)
            - [VRAM usage strategy (renderer\_strategy)](#vram-usage-strategy-renderer_strategy)
            - [Set disk type (disk\_readonly)](#set-disk-type-disk_readonly)
        - [\* Network class (network)](#-network-class-network)
            - [List all bridgeable network cards (get\_bridge\_card)](#list-all-bridgeable-network-cards-get_bridge_card)
            - [Set network bridge mode (bridge)](#set-network-bridge-mode-bridge)
            - [Set network to NAT mode (nat)](#set-network-to-nat-mode-nat)
            - [Set bridge IP mode to DHCP (bridge\_dhcp)](#set-bridge-ip-mode-to-dhcp-bridge_dhcp)
            - [Set bridge IP mode to static (bridge\_static)](#set-bridge-ip-mode-to-static-bridge_static)
        - [ADB class (adb)](#adb-class-adb)
            - [Get the emulator's ADB connection info (get\_connect\_info)](#get-the-emulators-adb-connection-info-get_connect_info)
            - [Tap screen (click)](#tap-screen-click)
            - [Swipe screen (swipe)](#swipe-screen-swipe)
            - [Input text (input\_text)](#input-text-input_text)
            - [Simulate key event (key\_event)](#simulate-key-event-key_event)
            - [Push file (push)](#push-file-push)
            - [Push file to Download directory (push\_download)](#push-file-to-download-directory-push_download)
            - [Pull file (pull)](#pull-file-pull)
            - [Clear app data (clear)](#clear-app-data-clear)
        - [GUI automation class (auto)](#gui-automation-class-auto)
            - [Process emulator live frames (create\_handle)](#process-emulator-live-frames-create_handle)
            - [Save emulator live frame (save)](#save-emulator-live-frame-save)
            - [Find the first image in a frame (locateOnScreen)](#find-the-first-image-in-a-frame-locateonscreen)
            - [Find the center of the first image in a frame (locateCenterOnScreen)](#find-the-center-of-the-first-image-in-a-frame-locatecenteronscreen)
            - [Find all images in a frame (locateAllOnScreen)](#find-all-images-in-a-frame-locateallonscreen)
            - [Get the center of a Box (center)](#get-the-center-of-a-box-center)
            - [Practical example](#practical-example)
    - [Supporting This Project](#supporting-this-project)

## Project Overview

This project is a Python API built on top of MuMu's ``MuMuManager.exe``. It lets you control most operations of the MuMu emulator from Python.

The project requires that you already have MuMu Emulator installed, with version `>=4.0.0`.

### Recent updates (1.1.0)

- Fixed shell-invocation compatibility for ADB tap/input commands on MuMu.
- Fixed cross-talk of `select` state under concurrency; the index context of a `Mumu` instance is now thread-isolated.
- `auto.create_handle` now accepts `backend` and `fps` parameters; default is `backend='auto'`.
- `backend='auto'` prefers the official MuMu high-performance screenshot SDK (`mumu_sdk`) and automatically falls back to `scrcpy` if it is unavailable.

## How to Use

Install this project into your Python environment.

```powershell
pip install mumu-python-api-wlkjyy
```

If you need the GUI automation extras (OpenCV + scrcpy):

```powershell
pip install "mumu-python-api-wlkjyy[auto]"
```

Import the module.

```python
from mumu.mumu import Mumu
```

### Setting the MuMuManager Path

If your MuMu emulator is not installed at the ``default path``, you need to pass the path of MuMuManager when creating the Mumu object.
The default path is ``C:\Program Files\Netease\MuMu Player 12\shell\MuMuManager.exe``.

```python
from mumu.mumu import Mumu

Mumu(r'your_path').select(1)
```

### Emulator Index Explained

In the MuMu emulator, operations target an emulator by its index. The index can be specified at creation time or assigned automatically. If you don't know the index of your emulator, open the "MuMu Multi-Instance Manager", find your emulator, and the leading number is the index.

### Selecting an Emulator

If an operation needs to act on an emulator, use the ``select`` method to choose one.

```python
from mumu.mumu import Mumu

mumu = Mumu().select(1)
```

To select multiple emulators, the following four forms are equivalent and all select emulators 1, 2, and 3.

```python
from mumu.mumu import Mumu

# Form 1
mumu = Mumu().select([1, 2, 3])
# Form 2
mumu = Mumu().select(1, 2, 3)
# Form 3
mumu = Mumu().select((1, 2, 3))
# Forms can also be mixed
mumu = Mumu().select([1, 2], 3)
```

To select all emulators, use either of the following.

```python
from mumu.mumu import Mumu

# Form 1
mumu = Mumu().select()  # Calling select with no arguments selects all emulators
# Form 2: select all emulators via the all method
mumu = Mumu().all()
```

### An Example

Suppose I want to enable root on emulator 1 and then launch it.

```python
from mumu.mumu import Mumu

# Select emulator with index 1
mumu = Mumu().select(1)
# Enable root permission
mumu.permission.root.enable()
# Launch the emulator
mumu.power.start()
```

### Note

Classes marked with `*` are `super-classes` provided by this project; they are not part of the native MuMu API.

In multi-threaded scenarios, it is recommended to call `select(...)` once per thread before invoking the API, to avoid sharing an unselected-index object across threads.

## API Classes

This project provides a number of operation classes that you can use to control the emulator.

### Driver class (driver)

Note: Per the official documentation, only the network bridge driver is currently supported.

#### Network bridge driver (bridge)

##### Install the bridge driver (install)

Note: installing the bridge driver requires administrator privileges.

```python
Mumu().driver.bridge.install()
```

##### Uninstall the bridge driver (uninstall)

Note: uninstalling the bridge driver requires administrator privileges.

```python
Mumu().driver.bridge.uninstall()
```

### Permission class (permission)

####                * ROOT permission (root)

##### Enable ROOT permission (enable)

Note: enabling ROOT must be done while the emulator is shut down.

```python
Mumu().select('your_index').permission.root.enable()
```

##### Disable ROOT permission (disable)

Note: disabling ROOT must be done while the emulator is shut down.

```python
Mumu().select('your_index').permission.root.disable()
```

### Power class (power)

#### Start the emulator (start)

```python
Mumu().select('your_index').power.start()
```

Launch the specified app once the emulator finishes starting.

```python
Mumu().select('your_index').power.start('com.tencent.mobileqq')
```

#### Shut down the emulator (shutdown|stop)

```python
Mumu().select('your_index').power.shutdown()
# or
Mumu().select('your_index').power.stop()
```

#### Restart the emulator (restart|reboot)

```python
Mumu().select('your_index').power.restart()
# or
Mumu().select('your_index').power.reboot()
```

### Window class (window)

#### Show window (show)

```python
Mumu().select('your_index').window.show()
```

#### Hide window (hidden)

```python
Mumu().select('your_index').window.hidden()
```

#### Adjust window size or position (layout)

This method accepts 4 arguments: x coordinate, y coordinate, width, and height.

```python
Mumu().select('your_index').window.layout(0, 0, 800, 600)
```

To adjust only the window size:

```python
Mumu().select('your_index').window.layout(None, None, 1080, 1920)
```

You can also adjust a single argument.

```python
Mumu().select('your_index').window.layout(300, None, None, None)
# or
Mumu().select('your_index').window.layout(None, None, 1080, None)
```

### App class (app)

#### Install an app (install)

This method accepts one argument, the path to an APK file. If the APK path is unreachable, ``FileNotFoundError`` is raised.

```python
Mumu().select('your_index').app.install(r'C:\test.apk')
```

#### Uninstall an app (uninstall)

This method accepts one argument: the app's package name.

```python
Mumu().select('your_index').app.uninstall('com.miHoYo.Yuanshen')
```

#### Launch an app inside the emulator (launch)

This method accepts one argument: the app's package name.

```python
# Launch Genshin Impact
Mumu().select('your_index').app.launch('com.miHoYo.Yuanshen')
```

#### Close an app inside the emulator (close)

This method accepts one argument: the app's package name.

```python
# Close Genshin Impact
Mumu().select('your_index').app.close('com.miHoYo.Yuanshen')
```

####                * Check whether an app exists (exists)

This method accepts one argument: the app's package name.

```python
# Check whether Genshin Impact is installed
if (Mumu().select('your_index').app.exists('com.miHoYo.Yuanshen')):
    print('Genshin Impact is installed')
else:
    print('Genshin Impact is not installed')
```

####                * Check whether an app does not exist (doesntExists)

This method accepts one argument: the app's package name.

```python
# Check whether Genshin Impact is not installed
if (Mumu().select('your_index').app.doesntExists('com.miHoYo.Yuanshen')):
    print('Genshin Impact is not installed')
else:
    print('Genshin Impact is installed')
```

#### Get the list of installed apps (get_installed)

```python
# Get the list of installed apps
Mumu().select(1).app.get_installed()
```

Returns a list. When no apps are installed, returns an empty list.

```python
[
    {
        'package': 'com.miHoYo.Yuanshen',  # package name
        'app_name': 'Genshin Impact',  # app name
        'version': '4.1.8'  # version
    },
]
```

####                * Get app state (state)

This method accepts one argument (the app's package name) and returns a string: `running` means the app is running, `stopped` means the app is not running, and `not_installed` means the app is not installed.

```python
# Get Genshin Impact's state
Mumu().select('your_index').app.state('com.miHoYo.Yuanshen')
```

### Core class (core)

#### Create an emulator (create)

This method accepts one argument (the number of emulators to create) and returns a list of the indices of the created emulators.

Example: create one emulator.

```python
Mumu().core.create()
```

Example: create 5 emulators.

```python
Mumu().core.create(5)
```

Example: create an emulator with index ``10``.

```python
Mumu().select(10).core.create()
```

Create 5 emulators starting from index 3.

```python
Mumu().select(3).core.create(5)
```

Starting from indices 3 and 20, create 10 emulators each, with indices increasing sequentially (i.e. emulators with indices 3-12 and 20-29).

```python
Mumu().select(3, 20).core.create(10)
```

#### Clone an emulator (clone)

This method accepts one argument (the number of clones). An emulator must be selected before calling this method. It returns a list of the indices of the created emulators.

Example: clone the emulator with index 2.

```python
Mumu().select(2).core.clone()
```

Example: clone the emulators with indices 2, 4, and 6.

```python
Mumu().select(2, 4, 6).core.clone()
```

Example: clone the emulator with index 2 ten times.

```python
Mumu().select(2).core.clone(10)
```

Example: clone all emulators.

```python
Mumu().all().core.clone()
```

#### Delete an emulator (delete)

This method takes no arguments. An emulator must be selected before calling it. It returns a bool indicating whether the deletion succeeded.

Example: delete the emulator with index 2.

```python
if Mumu().select(2).core.delete():
    print('Deleted successfully')
```

Example: delete the emulators with indices 2, 4, and 6.

```python
Mumu().select(2, 4, 6).core.delete()
```

Example: delete all emulators (dangerous).

```python
Mumu().all().core.delete()
```

#### Rename an emulator (rename)

This method accepts one argument (the new emulator name). An emulator must be selected before calling it. It returns a bool indicating whether the rename succeeded.

Example: rename the emulator with index 2 to "test".

```python
if Mumu().select(2).core.rename('test'):
    print('Renamed successfully')
```

Example: rename the emulators with indices 2, 4, and 6 to "test".

```python
Mumu().select(2, 4, 6).core.rename('test')
```

Example: rename all emulators to "test".

```python
Mumu().all().core.rename('test')
```

#### Back up an emulator (export)

This method accepts three arguments. An emulator must be selected before calling it. It returns a bool indicating whether the backup succeeded.

| Parameter | Description           |
|-----------|-----------------------|
| dir       | Backup directory      |
| name      | Backup name           |
| zip       | Use zip compression   |

Example: back up the emulator with index 2 to the C: drive's `backup` directory with the name `test.mumudata`, uncompressed.

```python
if Mumu().select(2).core.export(r'C:\backup', 'test'):
    print('Backup successful')
```

Example: back up the emulators with indices 2, 4, and 6 to the C: drive's `backup` directory; the file names are derived from `test` with auto-appended suffixes, uncompressed.

```python
Mumu().select(2, 4, 6).core.export(r'C:\backup', 'test')
```

Example: back up all emulators to the C: drive's `backup` directory; the file names are derived from `test` with auto-appended suffixes, compressed.

```python
Mumu().all().core.export(r'C:\backup', 'test', True)
```

#### Import an emulator (import_)

This method accepts one argument: the path to a backup file. If a list is passed, multiple files are imported. An emulator must be selected before calling it. It returns a bool indicating whether the import succeeded.

Example: import `test.mumudata` from the C: drive to create an emulator.

```python
if Mumu().select(2).core.import_(r'C:\test.mumudata'):
    print('Imported successfully')
```

Example: import `test.mumudata` from the C: drive to create emulators, 10 times.

```python
Mumu().select(2).core.import_(r'C:\test.mumudata', 10)
```

Example: import `test.mumudata` from the C: drive and `test2.mumudata` from the D: drive to create emulators, 10 times each.

```python
Mumu().select(2).core.import_([r'C:\test.mumudata', r'D:\test2.mumudata'], 10)
```

#### Limit CPU usage (limit_cpu)

This method accepts one argument: the CPU usage limit. An emulator must be selected before calling it. It returns a bool indicating whether the operation succeeded.

Example: limit the CPU of emulator 2 to 50%.

```python
Mumu().select(2).core.limit_cpu(50)
```

Example: limit the CPU of emulators 2, 4, and 6 to 50%.

```python
Mumu().select(2, 4, 6).core.limit_cpu(50)
```

Example: limit the CPU of all emulators to 50%.

```python
Mumu().all().core.limit_cpu(50)
```

### Android event class (androidEvent)

This class exposes Android event operations, which you can use to drive the emulator.

An emulator must be selected before calling any method on this class. Each method returns a bool indicating success.
Unless otherwise noted, methods take no arguments.

#### Rotate screen (rotate)

```python
Mumu().select(1).androidEvent.rotate()
```

#### Go to home screen (go_home)

```python
Mumu().select(1).androidEvent.go_home()
```

#### Back (back)

```python
Mumu().select(1).androidEvent.go_back()
```

#### Pin window on top (top_most)

```python
Mumu().select(1).androidEvent.top_most()
```

#### Fullscreen window (fullscreen)

```python
Mumu().select(1).androidEvent.fullscreen()
```

#### Shake (shake)

```python
Mumu().select(1).androidEvent.shake()
```

#### Screenshot (screenshot)

```python
Mumu().select(1).androidEvent.screenshot()
```

#### Volume up (volume_up)

```python
Mumu().select(1).androidEvent.volume_up()
```

#### Volume down (volume_down)

```python
Mumu().select(1).androidEvent.volume_down()
```

#### Volume mute (volume_mute)

```python
Mumu().select(1).androidEvent.volume_mute()
```

#### Task key (go_task)

```python
Mumu().select(1).androidEvent.go_task()
```

#### Set virtual location (location)

This method accepts two arguments: longitude and latitude.

Example: set the virtual location of emulator 2 to longitude 114.1, latitude -23.

```python
Mumu().select(2).androidEvent.location(114.1, -23)
```

Example: set the virtual location of emulators 2, 4, and 6 to longitude 114.1, latitude -23.

```python
Mumu().select(2, 4, 6).androidEvent.location(114.1, -23)
```

Example: set the virtual location of all emulators to longitude 114.1, latitude -23.

```python
Mumu().all().androidEvent.location(114.1, -23)
```

#### Set gyro sensor (gyro)

This method accepts three arguments: x, y, and z axes.

Example: set the gyro sensor of emulator 2 to X=40, Y=20, Z=30.

```python
Mumu().select(2).androidEvent.gyro(40, 20, 30)
```

Example: set the gyro sensor of emulators 2, 4, and 6 to X=40, Y=20, Z=30.

```python
Mumu().select(2, 4, 6).androidEvent.gyro(40, 20, 30)
```

Example: set the gyro sensor of all emulators to X=40, Y=20, Z=30.

```python
Mumu().all().androidEvent.gyro(40, 20, 30)
```

### Shortcut class (shortcut)

#### Create a desktop shortcut (create)

This method accepts three arguments: shortcut name, shortcut icon path, and app package name.

Example: create a desktop shortcut named `test` for emulator 2 using `C:\test.ico` as the icon, auto-launching Genshin Impact.

```python
Mumu().select(2).shortcut.create('test', r'C:\test.ico', 'com.miHoYo.Yuanshen')
```

Example: create a desktop shortcut named `test` for emulators 2, 4, and 6 using `C:\test.ico` as the icon, auto-launching Genshin Impact.

```python
Mumu().select(2, 4, 6).shortcut.create('test', r'C:\test.ico', 'com.miHoYo.Yuanshen')
```

Example: create a shortcut named `test` for all emulators using `C:\test.ico` as the icon, auto-launching Genshin Impact.

```python
Mumu().all().shortcut.create('test', r'C:\test.ico', 'com.miHoYo.Yuanshen')
```

#### Delete a desktop shortcut (delete)

This method takes no arguments. An emulator must be selected before calling it. It returns a bool indicating whether the deletion succeeded.

Example: delete the shortcut for emulator 2.

```python
Mumu().select(2).shortcut.delete()
```

Example: delete the shortcuts for emulators 2, 4, and 6.

```python
Mumu().select(2, 4, 6).shortcut.delete()
```

Example: delete the shortcuts for all emulators.

```python
Mumu().all().shortcut.delete()
```

### Simulation class (simulation)

This class exposes simulated-device operations. (These are largely cosmetic.)

#### Set MAC address (mac_address)

This method accepts one argument (the new MAC address). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

```python
Mumu().select(1).simulation.mac_address('00:11:22:33:44:55')
```

Example: generate a random MAC address for emulator 1; either form works.

```python
from mumu.constant import MacAddress

# Form 1: pass a MAC address
Mumu().select(1).simulation.mac_address(MacAddress.random())

# Form 2: with no argument, a random MAC address is generated
Mumu().select(1).simulation.mac_address() 
```

#### Set IMEI (imei)

Android 12 does not allow apps to read the IMEI.

This method accepts one argument (the new IMEI). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

```python
Mumu().select(1).simulation.imei('123456789012345')
```

Example: generate a random IMEI for emulator 1; either form works.

```python
from mumu.constant import IMEI

# Form 1: pass an IMEI
Mumu().select(1).simulation.imei(IMEI.random())

# Form 2: with no argument, a random IMEI is generated
Mumu().select(1).simulation.imei() 
```

#### Set IMSI (imsi)

Android 12 does not allow apps to read the IMSI.

This method accepts one argument (the new IMSI). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

```python
Mumu().select(1).simulation.imsi('460000000000000')
```

Example: generate a random IMSI for emulator 1; either form works.

```python
from mumu.constant import IMSI

# Form 1: pass an IMSI
Mumu().select(1).simulation.imsi(IMSI.random())

# Form 2: with no argument, a random IMSI is generated
Mumu().select(1).simulation.imsi() 
```

#### Set Android ID (android_id)

This method accepts one argument (the new Android ID). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

```python
Mumu().select(1).simulation.android_id('1234567890123456')
```

Example: generate a random Android ID for emulator 1; either form works.

```python
from mumu.constant import AndroidID

# Form 1: pass an Android ID
Mumu().select(1).simulation.android_id(AndroidID.random())

# Form 2: with no argument, a random Android ID is generated
Mumu().select(1).simulation.android_id() 
```

#### Set device model (model)

This method accepts one argument (the new device model). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

```python
Mumu().select(1).simulation.model('MI 10')
```

#### Set motherboard brand (brand)

This method accepts one argument (the new motherboard brand). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

```python
Mumu().select(1).simulation.brand('Xiaomi')
```

#### Set hardware manufacturer (solution)

This method accepts one argument (the new hardware manufacturer). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

```python
Mumu().select(1).simulation.solution('qcom')
```

#### Set phone number (phone_number)

Android 12 does not allow apps to read the phone number.

This method accepts one argument (the new phone number). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

```python
Mumu().select(1).simulation.phone_number('18888888888')
```

Example: set a random phone number; either form works.

```python
from mumu.constant import PhoneNumber

# Form 1: pass a phone number
Mumu().select(1).simulation.phone_number(PhoneNumber.random())

# Form 2: with no argument, a random phone number is generated
Mumu().select(1).simulation.phone_number() 
```

#### Set GPU model (gpu_model)

This method exposes 4 parameters; pass one of them.

Example: set the GPU model of emulator 1 to GeForce RTX 3090.

```python
Mumu().select(1).simulation.gpu_model('GeForce RTX 3090')
```

Example: set the GPU model of emulator 1 to the high-end preset.

```python
Mumu().select(1).simulation.gpu_model(top_model=True)
```

Example: set the GPU model of emulator 1 to the low-end preset.

```python
Mumu().select(1).simulation.gpu_model(low_model=True)
```

Example: set the GPU model of emulator 1 to the mid-range preset.

```python
Memu().select(1).simulation.gpu_model(middle_model=True)
```

### Setting class (setting)

This class exposes operations on the emulator's configuration file.

In the setting class, when no emulator is selected, the operations target the global configuration (i.e. the defaults).

#### Get all configuration items (all)

This method has one parameter `all_writable`. When `True`, it returns all writable configuration items; when `False`, it returns all configuration items. It returns a dict of key/value pairs.

Example: get all configuration items.

```python
Mumu().select(1).setting.all()
```

Example: get all writable configuration items.

```python
Mumu().select(1).setting.all(True)
```

#### Get one or more configuration items (get)

This method accepts one or more arguments specifying the configuration items to retrieve. When fetching a single item, it returns a string; when fetching multiple items, it returns a dict of key/value pairs.

Example: get one configuration item (returns a string).

```python
value = Mumu().select(1).setting.get('window_size_fixed')
```

Example: get multiple configuration items (returns a dict).

```python
dict_val = Mumu().select(1).setting.get('window_size_fixed', 'window_save_rect')
```

#### Set one or more configuration items (set)

This method accepts one or more arguments specifying the configuration items to set. It returns a bool indicating whether the change succeeded.

When the value is `None`, the default value is restored.

If a configuration key contains `.` or `-`, replace `.` with two `_` and `-` with three `_`.

Example: set the `window_size_fixed` configuration of emulator 2 to `true`.

```python
Mumu().select(2).setting.set(window_size_fixed=True)
```

Example: set the `window_size_fixed` configuration of emulator 2 to `false` and `window_save_rect` to `true`.

```python
Mumu().select(2).setting.set(window_size_fixed=False, window_save_rect=True)
```

Restore the `window_size_fixed` configuration of emulator 2 (uses the default value).

```python
Mumu().select(2).setting.set(window_size_fixed=None)
```

#### Set configuration from a JSON file (set_by_json)

This method accepts one argument: the path to a JSON file. It returns a bool indicating whether the change succeeded.

Example:

A UTF-8 encoded `test.json` file on the C: drive with the following contents:

```json
{
  "window_save_rect": "true",
  "window_size_fixed": "false"
}
```

Apply this configuration to emulator 2 via the JSON file.

```python
Mumu().select(2).setting.set_by_json(r'C:\test.json')
```

#### *Check whether a config equals a value (equal)

This method accepts two arguments: the configuration item and the value. It returns a bool indicating equality.

Example: check whether the `window_size_fixed` configuration of emulator 2 equals `true`.

```python
if Mumu().select(2).setting.equal('window_size_fixed', True):
    print('Equal')
else:
    print('Not equal')
```

#### *Check whether a config does not equal a value (not_equal)

This method accepts two arguments: the configuration item and the value. It returns a bool indicating inequality.

Example: check whether the `window_size_fixed` configuration of emulator 2 does not equal `true`.

```python
if Mumu().select(2).setting.not_equal('window_size_fixed', True):
    print('Not equal')
else:
    print('Equal')
```

#### *If a config equals a value, change it to another value (equal_then_set)

This method accepts three arguments: the configuration item, the value, and the new value. It returns a bool indicating whether the change succeeded.

Example: check whether the `window_size_fixed` configuration of emulator 2 equals `true`; if so, change it to `false`.

```python
Mumu().select(2).setting.equal_then_set('window_size_fixed', True, False)
```

#### *If a config does not equal a value, change it to another value (not_equal_then_set)

This method accepts three arguments: the configuration item, the value, and the new value. It returns a bool indicating whether the change succeeded.

When no new value is passed, the `value` argument is set automatically.

Example: check whether the `window_size_fixed` configuration of emulator 2 does not equal `true`; if not, change it to `true`.

```python
Mumu().select(2).setting.not_equal_then_set('window_size_fixed', True, True)

# or 

Mumu().select(2).setting.not_equal_then_set('window_size_fixed', True)
```



### *Screen class (screen)

This class exposes screen operations for the emulator.

#### Set emulator resolution (resolution)

This method accepts two arguments: width and height. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

Example: set the resolution of emulator 2 to 800x600.

```python
Mumu().select(2).screen.resolution(800, 600)
```

#### Set to phone resolution (resolution_mobile)

This method takes no arguments. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

This method sets the resolution to 1080x1920 with DPI 480.

Example: set emulator 2 to phone resolution.

```python
Mumu().select(2).screen.resolution_mobile()
```

#### Set to tablet resolution (resolution_tablet)

This method takes no arguments. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

This method sets the resolution to 1920x1080 with DPI 280.

Example: set emulator 2 to tablet resolution.

```python
Mumu().select(2).screen.resolution_tablet()
```

#### Set to ultrawide resolution (resolution_ultrawide)

This method takes no arguments. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

This method sets the resolution to 3200x1440 with DPI 400.

Example: set emulator 2 to ultrawide resolution.

```python
Mumu().select(2).screen.resolution_ultrawide()
```

#### Set emulator DPI (dpi)

This method accepts one argument (the new DPI). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

Example: set the DPI of emulator 2 to 240.

```python
Mumu().select(2).screen.dpi(240)
```

#### Set emulator brightness (brightness)

This method accepts one argument (the new brightness). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

The valid range is 0-100.

Example: set the brightness of emulator 2 to 50.

```python
Mumu().select(2).screen.brightness(50)
```

#### Set max frame rate (max_frame_rate)

This method accepts one argument (the new max frame rate). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

The valid range is 1-240.

Example: set the max frame rate of emulator 2 to 60.

```python
Mumu().select(2).screen.max_frame_rate(60)
# or
Mumu().select(2).screen.max_frame_rate()  # default is 60
```

#### Set dynamic frame rate adjustment (dynamic_adjust_frame_rate)

This method accepts two arguments: `enable` and `dynamic_low_frame_rate_limit`. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

----

| Parameter                    | Type | Description                                                              |
|------------------------------|------|--------------------------------------------------------------------------|
| enable                       | bool | Whether to enable dynamic frame rate adjustment                          |
| dynamic_low_frame_rate_limit | int  | Frame rate to drop to when the emulator window is not in focus, default: 15 |

----

Example: enable dynamic frame rate adjustment for emulator 2, dropping to 15 fps.

```python
Mumu().select(2).screen.dynamic_adjust_frame_rate(True, 15)
```

Example: disable dynamic frame rate adjustment for emulator 2.

```python
Mumu().select(2).screen.dynamic_adjust_frame_rate(False)
```

#### Set vertical sync (vertical_sync)

This method accepts one argument: `enable`. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

Example: enable vertical sync for emulator 2.

```python
Mumu().select(2).screen.vertical_sync(True)
```

Example: disable vertical sync for emulator 2.

```python
Mumu().select(2).screen.vertical_sync(False)
```

#### Show frame rate (show_frame_rate)

This method accepts one argument: `enable`. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

Example: enable frame-rate display for emulator 2.

```python
Mumu().select(2).screen.show_frame_rate(True)
```

Example: disable frame-rate display for emulator 2.

```python
Mumu().select(2).screen.show_frame_rate(False)
```

#### Auto-rotate window (window_auto_rotate)

This method accepts one argument: `enable`. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

When enabled, the emulator window will rotate automatically based on the running app.

Example: enable window auto-rotate for emulator 2.

```python
Mumu().select(2).screen.window_auto_rotate(True)
```

Example: disable window auto-rotate for emulator 2.

```python
Mumu().select(2).screen.window_auto_rotate(False)
```

### Performance class (performance)

This class exposes performance operations for the emulator.

All operations in this class take effect after the emulator is restarted.

#### Set CPU and memory (set)

This method accepts two arguments: CPU count and memory size. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

The CPU count range is 1-16.

The memory size range is 1-16 (in GB, integers only).

Example: set emulator 2 to 4 CPU cores and 4 GB of memory.

```python
Mumu().select(2).performance.set(4, 4)
```

#### Set CPU count (cpu)

This method accepts one argument (the CPU count). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

The CPU count range is 1-16.

Example: set emulator 2 to 4 CPU cores.

```python
Mumu().select(2).performance.cpu(4)
```

#### Set memory size (memory)

This method accepts one argument (the memory size). An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

The memory size range is 1-16 (in GB, integers only).

Example: set emulator 2 to 4 GB of memory.

```python
Mumu().select(2).performance.memory(4)
```

#### Force discrete graphics (force_discrete_graphics)

This method accepts one argument: `enable`. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

Example: enable forced discrete graphics for emulator 2.

```python
Mumu().select(2).performance.force_discrete_graphics(True)
```

Example: disable forced discrete graphics for emulator 2.

```python
Mumu().select(2).performance.force_discrete_graphics(False)
```

#### VRAM usage strategy (renderer_strategy)

This method accepts three parameters; pass one of them.

Example: set the VRAM usage strategy of emulator 2 to auto.

```python
Mumu().select(2).performance.renderer_strategy(auto=True)
# or
Mumu().select(2).performance.renderer_strategy()
```

Example: set the VRAM usage strategy of emulator 2 to "lower resource usage".

```python
Mumu().select(2).performance.renderer_strategy(perf=True)
```

Example: set the VRAM usage strategy of emulator 2 to "better visual quality".

```python
Mumu().select(2).performance.renderer_strategy(dis=True)
```

#### Set disk type (disk_readonly)

This method accepts one argument: `enable`. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

The default for `enable` is `True`. When enabled, the disk type is "read-only system disk" (officially recommended); when disabled, the disk type is "writable system disk".

This method also exposes a helper `disk_writable` for setting the disk type to writable.

Example: set the disk type of emulator 2 to read-only system disk.

```python
Mumu().select(2).performance.disk_readonly(True)

# or

Mumu().select(2).performance.disk_readonly()
```

Example: set the disk type of emulator 2 to writable system disk.

```python
Mumu().select(2).performance.disk_readonly(False)

# or

Mumu().select(2).performance.disk_writable()
```

### *Network class (network)

This class exposes network operations for the emulator.

#### List all bridgeable network cards (get_bridge_card)

This method returns a list of all bridgeable network cards.

Example: get all bridgeable network cards.

```python
Mumu().select(1).network.get_bridge_card()
```

Example return:

```python
['Realtek Gaming GbE Family Controller', 'Sangfor SSL VPN CS Support System VNIC', 'Microsoft KM-TEST Loopback Adapter',
 'Intel(R) Wi-Fi 6E AX211 160MHz']
```

#### Set network bridge mode (bridge)

This method accepts two arguments: whether to enable bridging and the network card name. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

This method requires the "bridge driver" to be installed.

Example: enable bridge mode for emulator 2 with the card `Realtek Gaming GbE Family Controller`.

```python
Mumu().select(2).network.bridge(True, 'Realtek Gaming GbE Family Controller')
```

Example: disable bridge mode for emulator 2.

```python
Mumu().select(2).network.bridge(False)
```

#### Set network to NAT mode (nat)

This method takes no arguments. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

Example: set the network of emulator 2 to NAT mode.

```python
Mumu().select(2).network.nat()
```

#### Set bridge IP mode to DHCP (bridge_dhcp)

This method takes no arguments. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

Example: set the bridge IP mode of emulator 2 to DHCP.

```python
Mumu().select(2).network.bridge_dhcp()
```

#### Set bridge IP mode to static (bridge_static)

This method accepts 5 arguments: IP address, subnet mask, gateway, DNS1, and DNS2. An emulator must be selected before calling it. It returns a bool indicating whether the change succeeded.

When the DNS arguments are omitted, the defaults are DNS1 = `8.8.8.8` and DNS2 = `114.114.114.114`.

Example: set the bridge IP mode of emulator 2 to static, with IP `192.168.10.10`, subnet mask `255.255.255.0`,
and gateway `192.168.10.1`.

```python
Mumu().select(2).network.bridge_static('192.168.10.10', '255.255.255.0', '192.168.10.1')
```

### ADB class (adb)

This class exposes ADB operations.

#### Get the emulator's ADB connection info (get_connect_info)

This method takes no arguments. An emulator must be selected before calling it. When a single emulator is selected, it returns a tuple of (IP, port); when multiple emulators are selected, it returns a dict whose keys are indices and whose values are (IP, port) tuples.

If the ADB connection info cannot be retrieved for a selected emulator, `(None, None)` is returned.

Example: get the ADB connection info of emulator 2.

```python
adb_ipaddr, adb_port = Mumu().select(2).adb.get_connect_info()
```

Example: get the ADB connection info of emulators 2, 4, and 6.

```python
adb_info = Mumu().select(2, 4, 6).adb.get_connect_info()
```

Example return:

```python
{'2': ('172.30.20.123', 16416), '4': (None, None), '6': (None, None)}
```

#### Tap screen (click)

This method accepts two arguments: X and Y coordinates. An emulator must be selected before calling it. It returns a bool indicating whether the tap succeeded.

Example: tap (100, 100) on emulator 2.

```python
Mumu().select(2).adb.click(100, 100)
```

Example: tap (100, 100) on emulators 2, 4, and 6.

```python
Mumu().select(2, 4, 6).adb.click(100, 100)
```

#### Swipe screen (swipe)

This method accepts 5 arguments: starting X, starting Y, ending X, ending Y, and swipe duration. An emulator must be selected before calling it. It returns a bool indicating whether the swipe succeeded.

Example: swipe from (100, 100) to (200, 200) on emulator 2 over 500 ms.

```python
Mumu().select(2).adb.swipe(100, 100, 200, 200, 500)
#  or
Mumu().select(2).adb.swipe(100, 100, 200, 200)  # default is 500 ms
```

Example: swipe from (100, 100) to (200, 200) on emulators 2, 4, and 6 over 500 ms.

```python
Mumu().select(2, 4, 6).adb.swipe(100, 100, 200, 200, 500)
```

#### Input text (input_text)

This method accepts one argument (the text to input). An emulator must be selected before calling it. It returns a bool indicating whether the input succeeded.

Example: type `Hello World` on emulator 2.

```python
Mumu().select(2).adb.input_text('Hello World')
```

Example: type `Hello World` on emulators 2, 4, and 6.

```python
Mumu().select(2, 4, 6).adb.input_text('Hello World')
```

#### Simulate key event (key_event)

This method accepts one argument (the key to simulate). An emulator must be selected before calling it. It returns a bool indicating whether the key event succeeded.

Example: simulate the `HOME` key on emulator 2.

```python
Mumu().select(2).adb.key_event(3)
```

Example: simulate the `HOME` key using the key constants this project provides.

```python
from mumu.constant import AndroidKey

Mumu().select(2).adb.key_event(AndroidKey.KEYCODE_HOME)
```

Example: simulate volume up on emulators 2, 4, and 6.

```python
from mumu.constant import AndroidKey

Mumu().select(2, 4, 6).adb.key_event(AndroidKey.KEYCODE_VOLUME_UP)
```

#### Push file (push)

This method accepts two arguments: the local file path and the emulator file path. An emulator must be selected before calling it. It returns a bool indicating whether the upload succeeded.

When the upload fails, a `warning` is emitted.

Example: push the local file `C:\test.txt` to `/sdcard/test.txt` on emulator 2.

```python
Mumu().select(2).adb.push(r'C:\test.txt', '/sdcard/test.txt')
```

Example: push the local file `C:\test.txt` to `/sdcard/test.txt` on emulators 2, 4, and 6.

```python
Mumu().select(2, 4, 6).adb.push(r'C:\test.txt', '/sdcard/test.txt')
```

#### Push file to Download directory (push_download)

This method accepts two arguments: the local file path and the file name on the emulator. An emulator must be selected before calling it. It returns a bool indicating whether the upload succeeded.

When `emulator file name` is `None`, the local file name is used automatically.

Example: push the local file `C:\test.txt` to the `Download` directory on emulator 2.

```python
Mumu().select(2).adb.push_download(r'C:\test.txt')
```

Example: push the local file `C:\test.txt` to the `Download` directory on emulators 2, 4, and 6 and rename it to `test1.txt`.

```python
Mumu().select(2, 4, 6).adb.push_download(r'C:\test.txt', 'test1.txt')
```

#### Pull file (pull)

This method accepts two arguments: the emulator file path and the local file path. An emulator must be selected before calling it. It returns a bool indicating whether the download succeeded.

When the download fails, a `warning` is emitted.

Example: pull `/sdcard/test.txt` from emulator 2 to local `C:\test.txt`.

```python
Mumu().select(2).adb.pull('/sdcard/test.txt', r'C:\test.txt')
```

#### Clear app data (clear)

This method accepts one argument (the app's package name). An emulator must be selected before calling it. It returns a bool indicating whether the clear succeeded.

If the package name is invalid, an exception is raised.

Example: clear app data on emulator 2.

```python
Mumu().select(2).adb.clear('com.miHoYo.Yuanshen')
```

### GUI automation class (auto)

This class exposes GUI automation for the emulator, e.g. driving operations via image, coordinate, or text matching.

Prerequisite: install the `opencv-python` library, e.g. `pip install opencv-python`.

Live frame capture supports two backends:

- `mumu_sdk` (recommended): uses MuMu's official high-performance screenshot API; usually faster.
- `scrcpy`: a compatibility backend; requires `scrcpy-client` (`pip install scrcpy-client`).

#### Process emulator live frames (create_handle)

This method accepts three arguments:

- `handle`: callback for processing frames.
- `backend`: `auto`/`mumu_sdk`/`scrcpy`, default `auto`.
- `fps`: only takes effect with `mumu_sdk`; the capture frame rate, default `30`.

When `backend='auto'`, `mumu_sdk` is preferred and falls back to `scrcpy` automatically if it is unavailable.

The `handle` callback takes two arguments, `frame` and `mumu`, representing the frame and the current emulator object.

`frame` is a `numpy` array and can be processed directly with `opencv` methods.
`mumu` is the current emulator object with only the current emulator selected (thread-isolated; you can call its API directly).

Example: process frames from emulator 2.

```python
def handle(frame, mumu):
    # do something
    print('Received frame from emulator:', mumu.core.utils.get_vm_id())


Mumu().select(2).auto.create_handle(handle)
```

Example: process frames from emulators 2, 4, and 6.

```python
def handle(frame, mumu):
    # do something
    print('Received frame from emulator:', mumu.core.utils.get_vm_id())


Mumu().select(2, 4, 6).auto.create_handle(handle)
```

Example: force the MuMu SDK and set the frame rate.

```python
Mumu().select(2).auto.create_handle(handle, backend='mumu_sdk', fps=60)
```

Example: force the scrcpy backend.

```python
Mumu().select(2).auto.create_handle(handle, backend='scrcpy')
```

#### Save emulator live frame (save)

This method accepts two arguments, `frame` and `path`, and saves the emulator frame.

Example: save a frame to `C:\test.png`.

```python
def handle(frame, mumu):
    mumu.auto.save(frame, r'C:\test.png')


Mumu().select(2).auto.create_handle(handle)
```

Example: save a frame from emulator 3 to `C:\test.png`.

```python
def handle(frame, mumu):
    if mumu.core.utils.get_vm_id() == '3':
        mumu.auto.save(frame, r'C:\test.png')


Mumu().select(2, 3).auto.create_handle(handle)
```

#### Find the first image in a frame (locateOnScreen)

This method accepts 4 arguments: `haystack`, `needle`, `confidence`, and `grayscale`, and searches for an image inside a frame.

`confidence` is the similarity threshold, in the range 0-1, default 0.8.

`grayscale` toggles grayscale matching; default `False`.

Example: find the image `C:\test.png` inside a frame.

```python
def handle(frame, mumu):
    # do something
    print('Received frame from emulator:', mumu.core.utils.get_vm_id())
    pos = mumu.auto.locateOnScreen(frame, r'C:\test.png')
    if pos:
        print('Image found:', pos)
    else:
        print('Image not found')
```

#### Find the center of the first image in a frame (locateCenterOnScreen)

This method accepts 4 arguments: `haystack`, `needle`, `confidence`, and `grayscale`, and searches for an image inside a frame.

`confidence` is the similarity threshold, in the range 0-1, default 0.8.

`grayscale` toggles grayscale matching; default `False`.

```python
def handle(frame, mumu):
    # do something
    print('Received frame from emulator:', mumu.core.utils.get_vm_id())
    pos = mumu.auto.locateCenterOnScreen(frame, r'C:\test.png')
    if pos:
        print('Image center found:', pos)
    else:
        print('Image not found')

```

#### Find all images in a frame (locateAllOnScreen)

This method accepts 4 arguments: `haystack`, `needle`, `confidence`, and `grayscale`, and searches for an image inside a frame.

`confidence` is the similarity threshold, in the range 0-1, default 0.8.
`grayscale` toggles grayscale matching; default `False`.

```python
def handle(frame, mumu):
    # do something
    print('Received frame from emulator:', mumu.core.utils.get_vm_id())
    pos = mumu.auto.locateAllOnScreen(frame, r'C:\test.png')
    if pos:
        print('Images found:', pos)
    else:
        print('Image not found')

```

#### Get the center of a Box (center)

This method accepts one argument, `box`, and returns the center of the box as (x, y).

`box` is a tuple of 4 elements: top-left x, top-left y, bottom-right x, and bottom-right y.

```python
def handle(frame, mumu):
    # do something
    print('Received frame from emulator:', mumu.core.utils.get_vm_id())
    pos = mumu.auto.locateOnScreen(frame, r'C:\test.png')
    if pos:
        print('Image found:', pos)
        x, y = mumu.auto.center(pos)
        print('Center:', x, y)
    else:
        print('Image not found')

```

#### Practical example

Listen for frames from emulator 3. When `test.png` appears, print "Found", along with the current time and the emulator ID, and then go back to the home screen.

```python
def handle(frame, mumu: Mumu):
    if mumu.auto.locateOnScreen(frame, './test.png', confidence=0.75, grayscale=True):
        print("Found", time.time(), 'on emulator', mumu.core.utils.get_vm_id())
        mumu.androidEvent.go_home()


Mumu().select(3).auto.create_handle(handle)

```

## Supporting This Project

Author: wlkjyy

Mail: <wlkjyy@vip.qq.com>

WeChat: laravel_debug
