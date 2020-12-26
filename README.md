# kivy-basics

Deployment instruction of a simple paint app from the
[Kivy tutorials](https://kivy.org/doc/stable/tutorials/firstwidget.html).

Except `main.py`, the rest of the project is in the public domain. Please
refer to the header comment of `main.py` for its license information.

The instruction is intended for when you are using Windows or OS X and
want to deploy the application using buildozer, but you do not want to
install buildozer or Linux. However, it assumes you have docker
installed and logged into Docker Hub. The steps are as follows.

1. Run the `kivy/buildozer` container in the following way:
   ```
   docker run -ti --entrypoint bash kivy/buildozer
   ```

2. Open another shell window of your host OS, and in it, check the
   name of the container given by docker:
   ```
   docker ps
   ```
   This command will show something like the following, and we will
   use the name `friendly_shtern` as an example (the name shown may be
   different in your case) for the rest of this instruction:
   ```
   17de1883695c   kivy/buildozer   "bash"    26 minutes ago   Up 26 minutes             friendly_shtern
   ```

3. In your host OS shell, copy `main.py` and `buildozer.spec` into the
   container:
   ```
   docker cp main.py friendly_shtern:/home/user/hostcwd/
   docker cp buildozer.spec friendly_shtern:/home/user/hostcwd/
   ```
   `main.py` is the simple paint app from the [Kivy
   tutorials](https://kivy.org/doc/stable/tutorials/firstwidget.html).

   The reason why we use copying instead of mounting a source
   directory using the `-v` option of `docker run` is because with
   mounting approach, buildozer may fail to unpack some gzipped tar
   files if the host OS is not Linux, such as OS X.

4. In the container's bash shell, do:
   ```
   sudo chown user:user .
   ```
   This is so that the current directory can be written by the current
   user.

5. Next, in the container's bash shell, do:
   ```
   buildozer -v android debug
   ```
   When asked to accept Android SDK license, input `y`. This step
   should produce an apk file named
   `paint-2.0.0-armeabi-v7a-debug.apk` in the `bin/` subdirectory in
   the container.

6. Copy the apk file to your host OS:
   ```
   docker cp friendly_shtern:/home/user/hostcwd/bin/paint-2.0.0-armeabi-v7a-debug.apk .
   ```

7. Upload the apk file from your host OS to Google drive, and then in
   your phone, install the apk from the Google drive. You may need to
   adjust the setting of your phone to allow apk installation from
   Google drive.
