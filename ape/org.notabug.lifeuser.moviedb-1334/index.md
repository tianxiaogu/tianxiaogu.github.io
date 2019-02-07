title: org.notabug.lifeuser.moviedb

# org.notabug.lifeuser.moviedb

[Google Play Store](https://play.google.com/store/apps/details?id=org.notabug.lifeuser.moviedb)

[Timeline](./vis-timeline.html)

<iframe src="./vis-timeline.html" width="100%" height="500px" style="border:none;"></iframe>

```
// java.lang.NumberFormatException: Invalid int: ""
// 	at java.lang.Integer.invalidInt(Integer.java:138)
// 	at java.lang.Integer.parseInt(Integer.java:358)
// 	at java.lang.Integer.parseInt(Integer.java:334)
// 	at org.notabug.lifeuser.moviedb.activity.DetailActivity$6.onFocusChange(DetailActivity.java:812)
// 	at android.view.View.onFocusChanged(View.java:5723)
// 	at android.widget.TextView.onFocusChanged(TextView.java:8224)
// 	at android.view.View.clearFocusInternal(View.java:5605)
// 	at android.view.View.clearFocus(View.java:5585)
// 	at android.view.ViewGroup.clearFocus(ViewGroup.java:981)
// 	at android.view.ViewGroup.clearFocus(ViewGroup.java:981)
// 	at android.view.ViewGroup.clearFocus(ViewGroup.java:981)
// 	at android.view.View.setFlags(View.java:10594)
// 	at android.view.View.setVisibility(View.java:7431)
// 	at org.notabug.lifeuser.moviedb.activity.DetailActivity$9.onAnimationStart(DetailActivity.java:890)
// 	at android.view.animation.Animation$1.run(Animation.java:362)
// 	at android.os.Handler.handleCallback(Handler.java:739)
// 	at android.os.Handler.dispatchMessage(Handler.java:95)
// 	at android.os.Looper.loop(Looper.java:148)
// 	at android.app.ActivityThread.main(ActivityThread.java:5417)
// 	at java.lang.reflect.Method.invoke(Native Method)
// 	at com.android.internal.os.ZygoteInit$MethodAndArgsCaller.run(ZygoteInit.java:726)
// 	at com.android.internal.os.ZygoteInit.main(ZygoteInit.java:616)

```



