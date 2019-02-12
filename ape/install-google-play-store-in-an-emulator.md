title: Install the Google Play Store in an Emulator

# Install the Google Play Store in an Emulator


1. Create an AVD using the Android Nexus 5 API 23 x86 image. By default, the name of the AVD should be `Nexus 5 API 23`.
    !!! note
        Android studio has officially released three types of emulators for **Nexus 5 API 23 x86**, i.e., with Google Play Store, with Google API only and without any Google stuffs.
        Here you must select the one without any Google stuffs since we will install a full Google service framework manually.
2. Follow instructions in <https://medium.com/@dai_shi/installing-google-play-services-on-an-android-studio-emulator-fffceb2c28a1>
3. By default, all permissions of Google Play Service have been disabled. You will encounter crashes as described in the previous link. To solve this issue, you must first enable location and then grant all permissions to Google Play Service.
