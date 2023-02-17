function categorizeEmails() {
    var threads = GmailApp.getInboxThreads();
    var label = GmailApp.createLabel("My Label");
    for (var i = 0; i < threads.length; i++) {
        var thread = threads[i];
        var subject = thread.getFirstMessageSubject().toLowerCase();
        if (subject.indexOf("keyword") !== -1 || subject.indexOf("sender") !== -1) {
            thread.addLabel(label);
            if (subject.indexOf("newsletter") !== -1 || subject.indexOf("social media") !== -1) {
                thread.moveToArchive();
            }
            if (subject.indexOf("snooze") !== -1) {
                var now = new Date();
                var tomorrow = new Date(now.getTime() + 24 * 60 * 60 * 1000);
                thread.snooze(tomorrow);
            }
        }
    }
}