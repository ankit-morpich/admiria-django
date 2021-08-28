$.sessionTimeout({
    keepAliveUrl: '../../Extra/Extra-pages/pages-blank',
    logoutButton: "logout",
    logoutUrl: '../../authentication/pages-login',
    redirUrl: '../../authentication/pages-lock-screen',
    warnAfter: 3e3,
    redirAfter: 3e4,
    countdownMessage: "Redirecting in {timer} seconds.",
});