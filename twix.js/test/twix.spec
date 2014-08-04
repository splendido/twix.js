<!DOCTYPE html><html><head><title>Twix.js</title><link href="/stylesheets/twix.css" rel="stylesheet" type="text/css" /><script src="/javascripts/twix-site.js" type="text/javascript"></script></head><body><div id="navbar"><div class="container"><div class="pull-left" id="title"><a href="/">Twix.js</a></div><ul class="nav nav-pills pull-right"><li><a href="/">Home</a></li><li><a href="/docs.html">Docs</a></li><li><a href="https://github.com/icambron/twix.js">Github</a></li></ul></div></div>(function() {
  var Twix, moment, test, _ref, _ref1;

  test = function(moment, Twix) {
    var assertEqual, assertMomentEqual, assertTwixEqual, nextYear, thatDay, thisYear, tomorrow, yesterday;
    moment.lang('en');
    assertEqual = function(a, b) {
      if (a !== b) {
        throw new Error("Found " + b + ", expected " + a);
      }
    };
    assertTwixEqual = function(a, b) {
      if (!a.equals(b)) {
        throw new Error("Found " + (b.toString()) + ", expected " + (a.toString()));
      }
    };
    assertMomentEqual = function(a, b) {
      if (a.valueOf() !== b.valueOf()) {
        throw new Error("Found " + (b.format()) + ", expected " + (a.format()));
      }
    };
    thisYear = function(partial, time) {
      var fullDate;
      fullDate = "" + (moment().year()) + "-" + partial;
      if (time) {
        fullDate += "T" + time;
      }
      return moment(fullDate);
    };
    nextYear = function(partial, time) {
      return thisYear(partial, time).add(1, "year");
    };
    yesterday = function() {
      return moment().subtract(1, "day").startOf("day");
    };
    tomorrow = function() {
      return moment().add(1, "day").startOf("day");
    };
    thatDay = function(start, end) {
      if (start) {
        return moment("1982-05-25T" + start).twix("1982-05-25T" + end);
      } else {
        return moment("1982-05-25").twix("1982-05-25", true);
      }
    };
    describe("plugin", function() {
      describe("static constructor", function() {
        it("is the same as instantiating via the contructor", function() {
          assertEqual("function", typeof moment.twix);
          return assertTwixEqual(new Twix("1982-05-25", "1983-05-25", true), moment.twix("1982-05-25", "1983-05-25", true));
        });
        return it("uses the parse format for both dates", function() {
          return assertTwixEqual(new Twix(moment("2012-05-25"), moment("2013-05-25"), false), moment.twix("05/25/2012", "05/25/2013", "MM/DD/YYYY"));
        });
      });
      describe("create from a member", function() {
        it("is a function", function() {
          return assertEqual("function", typeof (moment().twix));
        });
        it("is the same as instantiating via the contructor", function() {
          return assertTwixEqual(new Twix("1982-05-25", "1983-05-25", false), moment("1982-05-25").twix("1983-05-25"));
        });
        it("accepts an allDay argument", function() {
          var t;
          t = moment("1982-05-25").twix("1983-05-25", true);
          return assertEqual(t.allDay, true);
        });
        it("uses the parse format", function() {
          return assertTwixEqual(new Twix(moment("2012-05-25"), moment("2013-05-25"), false), moment("05/25/2012").twix("05/25/2013", "MM/DD/YYYY"));
        });
        it("uses a parseStrict object argument", function() {
          var t;
          t = moment("05-25-1981").twix("A05/25/1982", "MM/DD/YYYY", {
            parseStrict: true
          });
          assertEqual(t.end.isValid(), false);
          t = moment("05-25-1981").twix("05/25/1982", "MM/DD/YYYY", {
            parseStrict: true
          });
          return assertEqual(t.end.isValid(), true);
        });
        return it("uses an allDay option argument", function() {
          var t;
          t = moment("05-25-1981").twix("05/25/1982", "MM/DD/YYYY", {
            allDay: true
          });
          assertEqual(t.allDay, true);
          t = moment("05-25-1981").twix("1982-05-25", {
            allDay: true
          });
          return assertEqual(t.allDay, true);
        });
      });
      describe("moment.forDuration()", function() {
        it("constructs a twix", function() {
          var duration, from, to, twix;
          from = thisYear("05-25");
          to = thisYear("05-26");
          duration = moment.duration(to.diff(from));
          twix = from.forDuration(duration);
          return assertTwixEqual(new Twix(from, to), twix);
        });
        return it("constructs an all-day twix", function() {
          var duration, from, to, twix;
          from = thisYear("05-25");
          to = thisYear("05-26");
          duration = moment.duration(to.diff(from));
          twix = from.forDuration(duration, true);
          return assertTwixEqual(new Twix(from, to, true), twix);
        });
      });
      describe("duration.afterMoment()", function() {
        it("contructs a twix", function() {
          var d, twix;
          d = moment.duration(2, "days");
          twix = d.afterMoment(thisYear("05-25"));
          return assertTwixEqual(new Twix(thisYear("05-25"), thisYear("05-27")), twix);
        });
        it("can use text", function() {
          var d, twix;
          d = moment.duration(2, "days");
          twix = d.afterMoment("1982-05-25");
          return assertTwixEqual(new Twix("1982-05-25", "1982-05-27"), twix);
        });
        return it("contructs an all-day twix", function() {
          var d, twix;
          d = moment.duration(2, "days");
          twix = d.afterMoment(thisYear("05-25"), true);
          return assertTwixEqual(new Twix(thisYear("05-25"), thisYear("05-27"), true), twix);
        });
      });
      return describe("duration.beforeMoment()", function() {
        it("contructs a twix", function() {
          var d, twix;
          d = moment.duration(2, "days");
          twix = d.beforeMoment(thisYear("05-25"));
          return assertTwixEqual(new Twix(thisYear("05-23"), thisYear("05-25")), twix);
        });
        it("can use text", function() {
          var d, twix;
          d = moment.duration(2, "days");
          twix = d.beforeMoment("1982-05-25");
          return assertTwixEqual(new Twix("1982-05-23", "1982-05-25"), twix);
        });
        return it("contructs an all-day twix", function() {
          var d, twix;
          d = moment.duration(2, "days");
          twix = d.beforeMoment(thisYear("05-25"), true);
          return assertTwixEqual(new Twix(thisYear("05-23"), thisYear("05-25"), true), twix);
        });
      });
    });
    describe("isSame()", function() {
      describe("year", function() {
        it("returns true if they're the same year", function() {
          return assertEqual(true, moment("1982-05-25").twix("1982-10-14").isSame("year"));
        });
        return it("returns false if they're different years", function() {
          return assertEqual(false, moment("1982-05-25").twix("1983-10-14").isSame("year"));
        });
      });
      return describe("day", function() {
        it("returns true if they're the same day", function() {
          return assertEqual(true, moment("1982-05-25 05:30 AM").twix("1982-05-25 07:30 PM").isSame("day"));
        });
        it("returns false if they're different days day", function() {
          return assertEqual(false, moment("1982-05-25 05:30 AM").twix("1982-05-26 07:30 PM").isSame("day"));
        });
        return it("returns true they're in different UTC days but the same local days", function() {
          return assertEqual(true, moment("1982-05-25 05:30 AM").twix("1982-05-25 11:30 PM").isSame("day"));
        });
      });
    });
    describe("length()", function() {
      describe("no arguments", function() {
        return it("returns milliseconds", function() {
          var mom;
          mom = moment();
          return assertEqual(60 * 1000, mom.twix(mom.clone().add(1, 'minute')).length());
        });
      });
      describe("days", function() {
        it("returns 1 for yesterday - today", function() {
          return assertEqual(1, yesterday().twix(moment()).length("days"));
        });
        it("returns 1 for a one-day all-day range", function() {
          return assertEqual(1, moment().twix(moment(), true).length("days"));
        });
        return it("returns 2 for a two-day all-day range", function() {
          return assertEqual(2, yesterday().twix(moment(), true).length("days"));
        });
      });
      return describe("other", function() {
        it("returns the right number for a years", function() {
          return assertEqual(16, moment("1996-02-17").twix("2012-08-14").length("years"));
        });
        return it("returns the right number for a months", function() {
          return assertEqual(197, moment("1996-02-17").twix("2012-08-14").length("months"));
        });
      });
    });
    describe("count()", function() {
      describe("days", function() {
        it("returns 1 inside a day", function() {
          var end, range, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "14:00");
          range = moment(start).twix(end);
          return assertEqual(1, range.count("days"));
        });
        it("returns 2 if the range crosses midnight", function() {
          var end, range, start;
          start = thisYear("05-25", "16:00");
          end = thisYear("05-26", "03:00");
          range = moment(start).twix(end);
          return assertEqual(2, range.count("days"));
        });
        return it("works fine for all-day ranges", function() {
          var end, range, start;
          start = thisYear("05-25");
          end = thisYear("05-26");
          range = moment(start).twix(end, true);
          return assertEqual(2, range.count("days"));
        });
      });
      return describe("years", function() {
        it("returns 1 inside a year", function() {
          var end, start;
          start = thisYear("05-25");
          end = thisYear("05-26");
          return assertEqual(1, moment(start).twix(end).count("year"));
        });
        return it("returns 2 if the range crosses Jan 1", function() {
          var end, start;
          start = thisYear("05-25");
          end = nextYear("05-26");
          return assertEqual(2, moment(start).twix(end).count("year"));
        });
      });
    });
    describe("countInner()", function() {
      return describe("days", function() {
        it("defaults to milliseconds", function() {
          var end, range, start;
          start = thisYear("05-25", "13:00");
          end = thisYear("05-25", "13:01");
          range = moment(start).twix(end);
          return assertEqual(60000, range.countInner());
        });
        it("returns 0 inside a day", function() {
          var end, range, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "14:00");
          range = moment(start).twix(end);
          return assertEqual(0, range.countInner("days"));
        });
        it("returns 0 if the range crosses midnight but is still < 24 hours", function() {
          var end, range, start;
          start = thisYear("05-25", "16:00");
          end = thisYear("05-26", "03:00");
          range = moment(start).twix(end);
          return assertEqual(0, range.countInner("days"));
        });
        it("returns 0 if the range is > 24 hours but still doesn't cover a full day", function() {
          var end, range, start;
          start = thisYear("05-25", "16:00");
          end = thisYear("05-26", "17:00");
          range = moment(start).twix(end);
          return assertEqual(0, range.countInner("days"));
        });
        it("returns 1 if the range includes one full day", function() {
          var end, range, start;
          start = thisYear("05-24", "16:00");
          end = thisYear("05-26", "17:00");
          range = moment(start).twix(end);
          return assertEqual(1, range.countInner("days"));
        });
        it("returns 1 if the range includes one full day barely", function() {
          var end, range, start;
          start = thisYear("05-24");
          end = thisYear("05-25");
          range = moment(start).twix(end);
          return assertEqual(1, range.countInner("days"));
        });
        it("returns 2 if the range includes two full days", function() {
          var end, range, start;
          start = thisYear("05-23", "16:00");
          end = thisYear("05-26", "17:00");
          range = moment(start).twix(end);
          return assertEqual(2, range.countInner("days"));
        });
        it("returns 1 for a one-day all-day range", function() {
          var end, range, start;
          start = thisYear("05-25");
          end = thisYear("05-25");
          range = moment(start).twix(end, true);
          return assertEqual(1, range.countInner("days"));
        });
        it("returns 2 for a two-day all-day range", function() {
          var end, range, start;
          start = thisYear("05-25");
          end = thisYear("05-26");
          range = moment(start).twix(end, true);
          return assertEqual(2, range.countInner("days"));
        });
        return it("doesn't muck with the twix object", function() {
          var end, range, start;
          start = thisYear("05-25");
          end = thisYear("05-26");
          range = moment(start).twix(end);
          range.countInner("years");
          assertMomentEqual(thisYear("05-25"), range.start);
          return assertMomentEqual(thisYear("05-26"), range.end);
        });
      });
    });
    describe("iterate()", function() {
      describe("duration", function() {
        var assertSameMinute;
        assertSameMinute = function(first, second) {
          return assertEqual(true, first.isSame(second, "minute"));
        };
        it("provides 4 periods of 20 minutes (as duration) if the range is 1 hour", function() {
          var duration, end, iter, results, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "04:00");
          duration = moment.duration(20, 'minutes');
          iter = start.twix(end).iterate(duration);
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          assertSameMinute(start.clone().add('minutes', 20), results[1]);
          return assertEqual(4, results.length);
        });
        return it("provides 5 periods of 2 hours, 30 minutes and 20 seconds if the range is 10 hours and 2 minutes", function() {
          var duration, end, iter, results, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "13:01:20");
          duration = moment.duration({
            hours: 2,
            minutes: 30,
            seconds: 20
          });
          iter = start.twix(end).iterate(duration);
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          assertSameMinute(start.clone().add('minutes', 30).add('hours', 2).add('seconds', 20), results[1]);
          return assertEqual(5, results.length);
        });
      });
      describe("minutes", function() {
        var assertSameMinute;
        assertSameMinute = function(first, second) {
          return assertEqual(true, first.isSame(second, "minute"));
        };
        return it("provides 4 periods of 20 minutes if the range is 1 hour", function() {
          var end, iter, results, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "04:00");
          iter = start.twix(end).iterate(20, "minutes", 0);
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          assertSameMinute(start.clone().add('minutes', 20), results[1]);
          return assertEqual(4, results.length);
        });
      });
      describe("days", function() {
        var assertSameDay;
        assertSameDay = function(first, second) {
          return assertEqual(true, first.isSame(second, "day"));
        };
        it("provides 1 day if the range includes 1 day", function() {
          var end, iter, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "14:00");
          iter = start.twix(end).iterate("days");
          assertSameDay(thisYear("05-25"), iter.next());
          return assertEqual(null, iter.next());
        });
        it("provides 2 days if the range crosses midnight", function() {
          var end, iter, start;
          start = thisYear("05-25", "16:00");
          end = thisYear("05-26", "03:00");
          iter = start.twix(end).iterate("days");
          assertSameDay(start, iter.next());
          assertSameDay(end, iter.next());
          return assertEqual(null, iter.next());
        });
        it("provides 366 days if the range is a year", function() {
          var end, iter, results, start;
          start = thisYear("05-25", "16:00");
          end = thisYear("05-25", "03:00").add(1, "year");
          iter = start.twix(end).iterate("days");
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          return assertEqual(366, results.length);
        });
        it("provides 1 day for an all-day range", function() {
          var end, iter, start;
          start = thisYear("05-25");
          end = thisYear("05-25");
          iter = start.twix(end, true).iterate("days");
          assertSameDay(thisYear("05-25"), iter.next());
          return assertEqual(null, iter.next());
        });
        it("doesn't generate extra days when there's a min time", function() {
          var end, iter, start;
          start = thisYear("05-25", "16:00");
          end = thisYear("05-26", "03:00");
          iter = start.twix(end).iterate("days", 4);
          assertSameDay(thisYear("05-25"), iter.next());
          return assertEqual(null, iter.next());
        });
        return it("provides 1 day for all-day ranges when there's a min time", function() {
          var end, iter, start;
          start = thisYear("05-25");
          end = thisYear("05-25");
          iter = start.twix(end, true).iterate("days", 4);
          assertEqual(true, iter.hasNext());
          assertSameDay(start, iter.next());
          assertEqual(false, iter.hasNext());
          return assertEqual(null, iter.next());
        });
      });
      return describe("years", function() {
        var assertSameYear;
        assertSameYear = function(first, second) {
          return assertEqual(true, first.isSame(second, "year"));
        };
        it("provides 1 year if the range happens inside a year", function() {
          var end, iter, start;
          start = thisYear("05-25");
          end = thisYear("05-25");
          iter = start.twix(end).iterate("years");
          assertSameYear(start, iter.next());
          return assertEqual(null, iter.next());
        });
        it("provides 2 years if the range crosses Jan 1", function() {
          var end, iter, start;
          start = thisYear("05-25");
          end = nextYear("05-26");
          iter = start.twix(end).iterate("years");
          assertSameYear(start, iter.next());
          assertSameYear(end, iter.next());
          return assertEqual(null, iter.next());
        });
        return it("doesn't generate extra years when there's a min time", function() {
          var end, iter, range, start;
          start = thisYear("05-25", "16:00");
          end = nextYear("01-01", "03:00");
          range = moment(start).twix(end);
          iter = range.iterate("years", 4);
          assertSameYear(thisYear("05-25"), iter.next());
          return assertEqual(null, iter.next());
        });
      });
    });
    describe("iterateInner()", function() {
      describe("duration", function() {
        var assertSameMinute;
        assertSameMinute = function(first, second) {
          return assertEqual(true, first.isSame(second, "minute"));
        };
        it("provides 3 periods of 20 minutes (as duration) if the range is 1 hour", function() {
          var duration, end, iter, results, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "04:00");
          duration = moment.duration(20, 'minutes');
          iter = start.twix(end).iterateInner(duration);
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          assertSameMinute(start.clone().add('minutes', 20), results[1]);
          return assertEqual(3, results.length);
        });
        return it("provides 4 periods of 2 hours, 30 minutes and 20 seconds if the range is 10 hours and 1 minute 20 seconds", function() {
          var duration, end, iter, results, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "13:01:20");
          duration = moment.duration({
            hours: 2,
            minutes: 30,
            seconds: 20
          });
          iter = start.twix(end).iterateInner(duration);
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          assertSameMinute(start.clone().add('minutes', 30).add('hours', 2).add('seconds', 20), results[1]);
          return assertEqual(4, results.length);
        });
      });
      describe("minutes", function() {
        var assertSameMinute;
        assertSameMinute = function(first, second) {
          return assertEqual(true, first.isSame(second, "minute"));
        };
        it("provides 3 periods of 20 minutes if the range is 1 hour", function() {
          var end, iter, results, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "04:00");
          iter = start.twix(end).iterateInner("minutes", 20);
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          assertSameMinute(start.clone().add('minutes', 20), results[1]);
          return assertEqual(3, results.length);
        });
        return it("provides 24 periods of 60 minutes if the range is 24 hours", function() {
          var end, iter, results, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-26", "03:00");
          iter = start.twix(end).iterateInner("minutes", 60);
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          return assertEqual(24, results.length);
        });
      });
      describe("hours", function() {
        var assertSameHour;
        assertSameHour = function(first, second) {
          return assertEqual(true, first.isSame(second, "hour"));
        };
        return it("provides 3 periods of 2 hours if the range is 7 hours", function() {
          var end, iter, results, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "10:00");
          iter = start.twix(end).iterateInner("hours", 2);
          results = (function() {
            var _results;
            _results = [];
            while (iter.hasNext()) {
              _results.push(iter.next());
            }
            return _results;
          })();
          assertSameHour(start.clone().add('hours', 2), results[1]);
          return assertEqual(3, results.length);
        });
      });
      return describe("days", function() {
        var assertSameDay;
        assertSameDay = function(first, second) {
          return assertEqual(true, first.isSame(second, "day"));
        };
        it("is empty if the range starts and ends the same day", function() {
          var end, iter, start;
          start = thisYear("05-25", "03:00");
          end = thisYear("05-25", "14:00");
          iter = start.twix(end).iterateInner("days");
          assertEqual(false, iter.hasNext());
          return assertEqual(null, iter.next());
        });
        it("is empty if the range doesn't contain a whole day", function() {
          var end, iter, start;
          start = thisYear("05-25", "16:00");
          end = thisYear("05-26", "17:00");
          iter = start.twix(end).iterateInner("days");
          assertEqual(false, iter.hasNext());
          return assertEqual(null, iter.next());
        });
        it("provides 1 day if the range contains 1 full day", function() {
          var end, iter, start;
          start = thisYear("05-24", "16:00");
          end = thisYear("05-26", "03:00");
          iter = start.twix(end).iterateInner("days");
          assertSameDay(thisYear("05-25"), iter.next());
          return assertEqual(null, iter.next());
        });
        it("provides 1 day for an all-day range", function() {
          var end, iter, start;
          start = thisYear("05-25");
          end = thisYear("05-25");
          iter = start.twix(end, true).iterateInner("days");
          assertSameDay(thisYear("05-25"), iter.next());
          return assertEqual(null, iter.next());
        });
        return it("provides 2 days for a two-day all-day range", function() {
          var end, iter, start;
          start = thisYear("05-25");
          end = thisYear("05-26");
          iter = start.twix(end, true).iterateInner("days");
          assertEqual(true, iter.hasNext());
          assertSameDay(thisYear("05-25"), iter.next());
          assertEqual(true, iter.hasNext());
          assertSameDay(thisYear("05-26"), iter.next());
          return assertEqual(null, iter.next());
        });
      });
    });
    describe("humanizeLength()", function() {
      describe("all-day ranges", function() {
        it("formats single-day correctly", function() {
          return assertEqual("all day", new Twix("1982-05-25", "1982-05-25", true).humanizeLength());
        });
        return it("formats multiday correctly", function() {
          return assertEqual("3 days", new Twix("1982-05-25", "1982-05-27", true).humanizeLength());
        });
      });
      return describe("non-all-day ranges", function() {
        it("formats single-day correctly", function() {
          return assertEqual("4 hours", thatDay("12:00", "16:00").humanizeLength());
        });
        return it("formats multiday correctly", function() {
          return assertEqual("2 days", new Twix("1982-05-25", "1982-05-27").humanizeLength());
        });
      });
    });
    describe("isEmpty()", function() {
      it("returns true for empty ranges", function() {
        return assertEqual(true, thatDay("12:00", "12:00").isEmpty());
      });
      return it("returns false for empty ranges", function() {
        return assertEqual(false, thatDay("12:00", "13:00").isEmpty());
      });
    });
    describe("asDuration()", function() {
      return it("returns a duration object", function() {
        var duration;
        duration = yesterday().twix(tomorrow()).asDuration();
        assertEqual(true, moment.isDuration(duration));
        return assertEqual(2, duration.days());
      });
    });
    describe("isPast()", function() {
      describe("all-day ranges", function() {
        it("returns true for days in the past", function() {
          return assertEqual(true, yesterday().twix(yesterday(), true).isPast());
        });
        it("returns false for today", function() {
          var today;
          today = moment().startOf("day");
          return assertEqual(false, today.twix(today, true).isPast());
        });
        return it("returns false for days in the future", function() {
          return assertEqual(false, tomorrow().twix(tomorrow(), true).isPast());
        });
      });
      return describe("non-all-day ranges", function() {
        it("returns true for the past", function() {
          var nearerPast, past;
          past = moment().subtract(3, "hours");
          nearerPast = moment().subtract(2, "hours");
          return assertEqual(true, past.twix(nearerPast).isPast());
        });
        return it("returns false for the future", function() {
          var furtherFuture, future;
          future = moment().add(2, "hours");
          furtherFuture = moment().add(3, "hours");
          return assertEqual(false, future.twix(furtherFuture).isPast());
        });
      });
    });
    describe("isFuture()", function() {
      describe("all-day ranges", function() {
        it("returns false for days in the past", function() {
          return assertEqual(false, yesterday().twix(yesterday(), true).isFuture());
        });
        it("returns false for today", function() {
          var today;
          today = moment().startOf("day");
          return assertEqual(false, today.twix(today, true).isFuture());
        });
        return it("returns true for days in the future", function() {
          return assertEqual(true, tomorrow().twix(tomorrow(), true).isFuture());
        });
      });
      return describe("non-all-day ranges", function() {
        it("returns false for the past", function() {
          var nearerPast, past;
          past = moment().subtract(3, "hours");
          nearerPast = moment().subtract(3, "hours");
          return assertEqual(false, past.twix(nearerPast).isFuture());
        });
        return it("returns true for the future", function() {
          var furtherFuture, future;
          future = moment().add(2, "hours");
          furtherFuture = moment().add(3, "hours");
          return assertEqual(true, future.twix(furtherFuture).isFuture());
        });
      });
    });
    describe("isCurrent()", function() {
      describe("all-day ranges", function() {
        it("returns false for days in the past", function() {
          return assertEqual(false, yesterday().twix(yesterday(), true).isCurrent());
        });
        it("returns true for today", function() {
          var today;
          today = moment().startOf("day");
          return assertEqual(true, today.twix(today, true).isCurrent());
        });
        return it("returns false for days in the future", function() {
          return assertEqual(false, tomorrow().twix(tomorrow(), true).isCurrent());
        });
      });
      return describe("non-all-day ranges", function() {
        it("returns false for the past", function() {
          var nearerPast, past;
          past = moment().subtract(3, "hours");
          nearerPast = moment().subtract(2, "hours");
          return assertEqual(false, past.twix(nearerPast).isCurrent());
        });
        return it("returns false for the future", function() {
          var furtherFuture, future;
          future = moment().add(2, "hours");
          furtherFuture = moment().add(3, "hours");
          return assertEqual(false, future.twix(furtherFuture).isCurrent());
        });
      });
    });
    describe("contains()", function() {
      describe("non-all-day", function() {
        var end, range, start;
        start = thisYear("05-25", "06:00");
        end = thisYear("05-25", "07:00");
        range = start.twix(end);
        it("returns true for moments inside the range", function() {
          return assertEqual(true, range.contains(thisYear("05-25", "06:30")));
        });
        it("returns true for moments at the beginning of the range", function() {
          return assertEqual(true, range.contains(start));
        });
        it("returns true for moments at the end of the range", function() {
          return assertEqual(true, range.contains(end));
        });
        it("returns false for moments before the range", function() {
          return assertEqual(false, range.contains(thisYear("05-25", "05:30")));
        });
        return it("returns false for moments after the range", function() {
          return assertEqual(false, range.contains(thisYear("05-25", "08:30")));
        });
      });
      return describe("all-day", function() {
        var range, start;
        start = thisYear("05-25");
        range = start.twix(start, true);
        it("returns true for moments inside the range", function() {
          return assertEqual(true, range.contains(thisYear("05-25", "06:30")));
        });
        it("returns true for moments at the beginning of the range", function() {
          return assertEqual(true, range.contains(start));
        });
        it("returns true for moments at the end of the range", function() {
          return assertEqual(true, range.contains(start.clone().endOf("day")));
        });
        it("returns false for moments before the range", function() {
          return assertEqual(false, range.contains(thisYear("05-24")));
        });
        return it("returns false for moments after the range", function() {
          return assertEqual(false, range.contains(thisYear("05-26")));
        });
      });
    });
    describe("overlaps()", function() {
      var assertNoOverlap, assertOverlap, assertOverlapness, someDays, someTime;
      assertOverlap = function(first, second) {
        return assertOverlapness(true)(first, second);
      };
      assertNoOverlap = function(first, second) {
        return assertOverlapness(false)(first, second);
      };
      assertOverlapness = function(shouldOverlap) {
        return function(first, second) {
          assertEqual(shouldOverlap, first.overlaps(second));
          return assertEqual(shouldOverlap, second.overlaps(first));
        };
      };
      someTime = thatDay("05:30", "08:30");
      someDays = new Twix("1982-05-24", "1982-05-25", true);
      describe("non-all-day ranges", function() {
        it("returns false for a later range", function() {
          return assertNoOverlap(someTime, thatDay("09:30", "11:30"));
        });
        return it("returns false for an earlier range", function() {
          return assertNoOverlap(someTime, thatDay("03:30", "04:30"));
        });
      });
      it("returns true for a partially later range", function() {
        return assertOverlap(someTime, thatDay("08:00", "11:30"));
      });
      it("returns true for a partially earlier range", function() {
        return assertOverlap(someTime, thatDay("04:30", "06:30"));
      });
      it("returns true for an engulfed range", function() {
        return assertOverlap(someTime, thatDay("06:30", "07:30"));
      });
      it("returns true for an engulfing range", function() {
        return assertOverlap(someTime, thatDay("04:30", "09:30"));
      });
      it("returns false for a range that starts immediately afterwards", function() {
        return assertNoOverlap(someTime, thatDay("08:30", "09:30"));
      });
      it("returns false for a range that ends immediately before", function() {
        return assertNoOverlap(someTime, thatDay("04:30", "05:30"));
      });
      describe("one all-day range", function() {
        it("returns true for a partially later range", function() {
          return assertOverlap(thatDay(), new Twix("1982-05-25 20:00", "1982-05-26 05:00"));
        });
        it("returns true for a partially earlier range", function() {
          return assertOverlap(thatDay(), new Twix("1982-05-24 20:00", "1982-05-25 07:00"));
        });
        it("returns true for an engulfed range", function() {
          return assertOverlap(thatDay(), someTime);
        });
        it("returns true for an engulfing range", function() {
          return assertOverlap(thatDay(), new Twix("1982-05-24 20:00", "1982-05-26 05:00"));
        });
        it("returns true for a range which starts on the same day", function() {
          return assertOverlap(thatDay(), new Twix("1982-05-25", "1982-05-27"));
        });
        return it("returns true for a range which ends on the same day", function() {
          return assertOverlap(thatDay(), new Twix("1982-05-23", "1982-05-25", true));
        });
      });
      return describe("two all-day ranges", function() {
        it("returns false for a later range", function() {
          return assertNoOverlap(someDays, new Twix("1982-05-26", "1982-05-27", true));
        });
        it("returns false for an earlier range", function() {
          return assertNoOverlap(someDays, new Twix("1982-05-22", "1982-05-23", true));
        });
        it("returns true for a partially later range", function() {
          return assertOverlap(someDays, new Twix("1982-05-24", "1982-05-26", true));
        });
        it("returns true for a partially earlier range", function() {
          return assertOverlap(someDays, new Twix("1982-05-22", "1982-05-24", true));
        });
        it("returns true for an engulfed range", function() {
          return assertOverlap(someDays, new Twix("1982-05-25", "1982-05-25", true));
        });
        return it("returns true for an engulfing range", function() {
          return assertOverlap(someDays, new Twix("1982-05-22", "1982-05-28", true));
        });
      });
    });
    describe("engulfs()", function() {
      var assertEngulfing, assertNotEngulfing, someDays, someTime;
      assertEngulfing = function(first, second) {
        return assertEqual(true, first.engulfs(second));
      };
      assertNotEngulfing = function(first, second) {
        return assertEqual(false, first.engulfs(second));
      };
      someTime = thatDay("05:30", "08:30");
      someDays = new Twix("1982-05-24", "1982-05-25", true);
      describe("non-all-day ranges", function() {
        it("returns false for a later range", function() {
          return assertNotEngulfing(someTime, thatDay("09:30", "11:30"));
        });
        it("returns false for an earlier range", function() {
          return assertNotEngulfing(someTime, thatDay("03:30", "04:30"));
        });
        it("returns true for a partially later range", function() {
          return assertNotEngulfing(someTime, thatDay("08:00", "11:30"));
        });
        it("returns true for a partially earlier range", function() {
          return assertNotEngulfing(someTime, thatDay("04:30", "06:30"));
        });
        it("returns true for an engulfed range", function() {
          return assertEngulfing(someTime, thatDay("06:30", "07:30"));
        });
        return it("returns true for an engulfing range", function() {
          return assertNotEngulfing(someTime, thatDay("04:30", "09:30"));
        });
      });
      describe("one all-day range", function() {
        it("returns true for a partially later range", function() {
          return assertNotEngulfing(thatDay(), new Twix("1982-05-25 20:00", "1982-05-26 05:00"));
        });
        it("returns true for a partially earlier range", function() {
          return assertNotEngulfing(thatDay(), new Twix("1982-05-24", "20:00", "1982-05-25 07:00"));
        });
        it("returns true for an engulfed range", function() {
          return assertEngulfing(thatDay(), someTime);
        });
        return it("returns true for an engulfing range", function() {
          return assertNotEngulfing(thatDay(), new Twix("1982-05-24 20:00", "1982-05-26 05:00"));
        });
      });
      return describe("two all-day ranges", function() {
        it("returns false for a later range", function() {
          return assertNotEngulfing(someDays, new Twix("1982-05-26", "1982-05-27", true));
        });
        it("returns false for an earlier range", function() {
          return assertNotEngulfing(someDays, new Twix("1982-05-22", "1982-05-23", true));
        });
        it("returns true for a partially later range", function() {
          return assertNotEngulfing(someDays, new Twix("1982-05-24", "1982-05-26", true));
        });
        it("returns true for a partially earlier range", function() {
          return assertNotEngulfing(someDays, new Twix("1982-05-22", "1982-05-24", true));
        });
        it("returns true for an engulfed range", function() {
          return assertEngulfing(someDays, new Twix("1982-05-25", "1982-05-25", true));
        });
        return it("returns true for an engulfing range", function() {
          return assertNotEngulfing(someDays, new Twix("1982-05-22", "1982-05-28", true));
        });
      });
    });
    describe("merge()", function() {
      return it("calls union()", function() {
        return assertTwixEqual(new Twix("1982-05-24", "1982-05-26"), new Twix("1982-05-24", "1982-05-25").merge(new Twix("1982-05-25", "1982-05-26")));
      });
    });
    describe("union()", function() {
      var someDays, someTime;
      someTime = thatDay("05:30", "08:30");
      someDays = new Twix("1982-05-24", "1982-05-25", true);
      describe("non-all-day ranges", function() {
        it("spans a later time", function() {
          return assertTwixEqual(thatDay("05:30", "11:30"), someTime.union(thatDay("09:30", "11:30")));
        });
        it("spans an earlier time", function() {
          return assertTwixEqual(thatDay("03:30", "08:30"), someTime.union(thatDay("03:30", "04:30")));
        });
        it("spans a partially later range", function() {
          return assertTwixEqual(thatDay("05:30", "11:30"), someTime.union(thatDay("08:00", "11:30")));
        });
        it("spans a partially earlier range", function() {
          return assertTwixEqual(thatDay("04:30", "08:30"), someTime.union(thatDay("04:30", "06:30")));
        });
        it("isn't affected by engulfed ranges", function() {
          return assertTwixEqual(someTime, someTime.union(thatDay("06:30", "07:30")));
        });
        it("becomes an engulfing range", function() {
          return assertTwixEqual(thatDay("04:30", "09:30"), someTime.union(thatDay("04:30", "09:30")));
        });
        return it("spans adjacent ranges", function() {
          return assertTwixEqual(thatDay("05:30", "09:30"), someTime.union(thatDay("08:30", "09:30")));
        });
      });
      describe("one all-day range", function() {
        it("spans a later time", function() {
          return assertTwixEqual(new Twix("1982-05-24 00:00", "1982-05-26 07:00"), someDays.union(new Twix("1982-05-24 20:00", "1982-05-26 07:00")));
        });
        it("spans an earlier time", function() {
          return assertTwixEqual(new Twix("1982-05-23 08:00", moment("1982-05-25").endOf("day")), someDays.union(new Twix("1982-05-23 08:00", "1982-05-25 07:00")));
        });
        it("isn't affected by engulfing ranges", function() {
          return assertTwixEqual(new Twix("1982-05-24 00:00", moment("1982-05-25").endOf("day")), someDays.union(someTime));
        });
        return it("becomes an engulfing range", function() {
          return assertTwixEqual(new Twix("1982-05-23 20:00", "1982-05-26 08:30"), someDays.union(new Twix("1982-05-23 20:00", "1982-05-26 08:30")));
        });
      });
      return describe("two all-day ranges", function() {
        it("spans a later time", function() {
          return assertTwixEqual(new Twix("1982-05-24", "1982-05-28", true), someDays.union(new Twix("1982-05-27", "1982-05-28", true)));
        });
        it("spans an earlier time", function() {
          return assertTwixEqual(new Twix("1982-05-21", "1982-05-25", true), someDays.union(new Twix("1982-05-21", "1982-05-22", true)));
        });
        it("spans a partially later time", function() {
          return assertTwixEqual(new Twix("1982-05-24", "1982-05-26", true), someDays.union(new Twix("1982-05-25", "1982-05-26", true)));
        });
        it("spans a partially earlier time", function() {
          return assertTwixEqual(new Twix("1982-05-23", "1982-05-25", true), someDays.union(new Twix("1982-05-23", "1982-05-25", true)));
        });
        it("isn't affected by engulfing ranges", function() {
          return assertTwixEqual(someDays, someDays.union(thatDay()));
        });
        return it("becomes an engulfing range", function() {
          return assertTwixEqual(someDays, thatDay().union(someDays));
        });
      });
    });
    describe("intersection()", function() {
      var someDays, someTime;
      someTime = thatDay("05:30", "08:30");
      someDays = new Twix("1982-05-24", "1982-05-25", true);
      describe("non-all-day ranges", function() {
        it("does not intersect with a later time", function() {
          var intersection;
          intersection = someTime.intersection(thatDay("09:30", "11:30"));
          assertTwixEqual(thatDay("09:30", "08:30"), intersection);
          return assertEqual(false, intersection.isValid());
        });
        it("does not intersect with an earlier time", function() {
          var intersection;
          intersection = someTime.intersection(thatDay("03:30", "04:30"));
          assertTwixEqual(thatDay("05:30", "04:30"), intersection);
          return assertEqual(false, intersection.isValid());
        });
        it("intersects with a partially later range", function() {
          return assertTwixEqual(thatDay("08:00", "08:30"), someTime.intersection(thatDay("08:00", "11:30")));
        });
        it("intersects with a partially earlier range", function() {
          return assertTwixEqual(thatDay("05:30", "06:30"), someTime.intersection(thatDay("04:30", "06:30")));
        });
        it("intersects with an engulfed range", function() {
          return assertTwixEqual(thatDay("06:30", "07:30"), someTime.intersection(thatDay("06:30", "07:30")));
        });
        it("intersects with an engulfing range", function() {
          return assertTwixEqual(thatDay("05:30", "08:30"), someTime.intersection(thatDay("04:30", "09:30")));
        });
        return it("does not intersect an adjacent range", function() {
          return assertEqual(0, someTime.intersection(thatDay("08:30", "09:30")).length());
        });
      });
      describe("one all-day range", function() {
        it("intersects with a later time", function() {
          return assertTwixEqual(new Twix("1982-05-24 20:00", "1982-05-25 23:59:59.999"), someDays.intersection(new Twix("1982-05-24 20:00", "1982-05-26 07:00")));
        });
        it("intersects with an earlier time", function() {
          return assertTwixEqual(new Twix("1982-05-24 00:00", "1982-05-25 07:00"), someDays.intersection(new Twix("1982-05-23 08:00", "1982-05-25 07:00")));
        });
        it("intersects with an engulfed range", function() {
          return assertTwixEqual(new Twix("1982-05-25 05:30", "1982-05-25 08:30"), someDays.intersection(someTime));
        });
        return it("intersects with an engulfing range", function() {
          return assertTwixEqual(new Twix("1982-05-24 00:00", "1982-05-25 23:59:59.999"), someDays.intersection(new Twix("1982-05-23 20:00", "1982-05-26 08:30")));
        });
      });
      return describe("two all-day range", function() {
        it("does not intersect with a later time", function() {
          var intersection;
          intersection = someDays.intersection(new Twix("1982-05-27", "1982-05-28", true));
          assertTwixEqual(new Twix("1982-05-27", "1982-05-25", true), intersection);
          return assertEqual(false, intersection.isValid());
        });
        it("does not intersect with an earlier time", function() {
          var intersection;
          intersection = someDays.intersection(new Twix("1982-05-21", "1982-05-22", true));
          assertTwixEqual(new Twix("1982-05-24", "1982-05-22", true), intersection);
          return assertEqual(false, intersection.isValid());
        });
        it("intersects with a partially later time", function() {
          return assertTwixEqual(new Twix("1982-05-25", "1982-05-25", true), someDays.intersection(new Twix("1982-05-25", "1982-05-26", true)));
        });
        it("intersects with a partially earlier time", function() {
          return assertTwixEqual(new Twix("1982-05-24", "1982-05-25", true), someDays.intersection(new Twix("1982-05-23", "1982-05-25", true)));
        });
        it("intersects with an engulfed range", function() {
          return assertTwixEqual(thatDay(), someDays.intersection(thatDay()));
        });
        return it("intersects with an engulfing range", function() {
          return assertTwixEqual(thatDay(), thatDay().intersection(someDays));
        });
      });
    });
    describe("isValid()", function() {
      it("should validate an interval with an earlier start", function() {
        assertEqual(true, new Twix("1982-05-24", "1982-05-26").isValid());
        assertEqual(true, new Twix("1982-05-24", "1982-05-26", true).isValid());
        assertEqual(true, new Twix("1982-05-24 20:00", "1982-05-26 07:00").isValid());
        return assertEqual(true, new Twix("1982-05-24 20:00", "1982-05-26 07:00", true).isValid());
      });
      it("should validate an interval without range", function() {
        assertEqual(true, new Twix("1982-05-24", "1982-05-24").isValid());
        assertEqual(true, new Twix("1982-05-24", "1982-05-24", true).isValid());
        assertEqual(true, new Twix("1982-05-24 20:00", "1982-05-24 20:00").isValid());
        return assertEqual(true, new Twix("1982-05-24 20:00", "1982-05-24 20:00", true).isValid());
      });
      it("should not validate an interval with a later start", function() {
        assertEqual(false, new Twix("1982-05-26", "1982-05-24").isValid());
        assertEqual(false, new Twix("1982-05-26", "1982-05-24", true).isValid());
        assertEqual(false, new Twix("1982-05-26 07:00", "1982-05-24 20:00").isValid());
        return assertEqual(false, new Twix("1982-05-26 07:00", "1982-05-24 20:00", true).isValid());
      });
      return it("should validate a same day interval with a later start", function() {
        return assertEqual(true, new Twix("1982-05-24 20:00", "1982-05-24 00:00", true).isValid());
      });
    });
    describe("simpleFormat()", function() {
      it("provides a simple string when provided no options", function() {
        var s;
        s = yesterday().twix(tomorrow()).simpleFormat();
        return assertEqual(true, s.indexOf(" - ") > -1);
      });
      it("specifies '(all day)' if it's all day", function() {
        var s;
        s = yesterday().twix(tomorrow(), true).simpleFormat();
        return assertEqual(true, s.indexOf("(all day)") > -1);
      });
      it("accepts moment formatting options", function() {
        var s;
        s = thisYear("10-14").twix(thisYear("10-14")).simpleFormat("MMMM");
        return assertEqual("October - October", s);
      });
      it("accepts an allDay option", function() {
        var s;
        s = thisYear("05-25").twix(thisYear("5-26"), true).simpleFormat(null, {
          allDay: "(wayo wayo)"
        });
        return assertEqual(true, s.indexOf("(wayo wayo)") > -1);
      });
      it("removes the all day text if allDay is null", function() {
        var s;
        s = thisYear("05-25").twix(thisYear("5-26"), true).simpleFormat(null, {
          allDay: null
        });
        return assertEqual(true, s.indexOf("(all day)") === -1);
      });
      return it("accepts a custom template", function() {
        var s;
        s = thisYear("05-25").twix(thisYear("5-26"), true).simpleFormat(null, {
          template: function(first, second) {
            return "" + first + " | " + second;
          }
        });
        return assertEqual(true, s.indexOf("|") > -1);
      });
    });
    describe("format()", function() {
      test = function(name, t) {
        return it(name, function() {
          var twix;
          twix = new Twix(t.start, t.end, t.allDay);
          return assertEqual(t.result, twix.format(t.options));
        });
      };
      describe("simple ranges", function() {
        test("empty range", {
          start: "1982-05-25T05:30",
          end: "1982-05-25T05:30",
          result: ""
        });
        test("different year, different day shows everything", {
          start: "1982-05-25T05:30",
          end: "1983-05-26T15:30",
          result: "May 25, 1982, 5:30 AM - May 26, 1983, 3:30 PM"
        });
        test("this year, different day skips year", {
          start: thisYear("05-25", "05:30"),
          end: thisYear("05-26", "15:30"),
          result: "May 25, 5:30 AM - May 26, 3:30 PM"
        });
        test("this year, different day shows year if requested", {
          start: thisYear("05-25", "05:30"),
          end: thisYear("05-26", "15:30"),
          options: {
            implicitYear: false
          },
          result: "May 25, 5:30 AM - May 26, 3:30 PM, " + (new Date().getFullYear())
        });
        test("same day, different times shows date once", {
          start: "1982-05-25 05:30",
          end: "1982-05-25 15:30",
          result: "May 25, 1982, 5:30 AM - 3:30 PM"
        });
        test("same day, different times, same meridian shows date and meridiem once", {
          start: "1982-05-25T05:30",
          end: "1982-05-25T06:30",
          result: "May 25, 1982, 5:30 - 6:30 AM"
        });
        test("custom month format for regular range", {
          start: "2010-08-25T05:30",
          end: "2010-08-25T06:30",
          options: {
            monthFormat: "MMMM"
          },
          result: "August 25, 2010, 5:30 - 6:30 AM"
        });
        return test("custom month format for all day range", {
          start: "2010-08-25",
          end: "2010-08-25",
          allDay: true,
          options: {
            monthFormat: "MMMM"
          },
          result: "August 25, 2010"
        });
      });
      describe("rounded times", function() {
        test("round hour doesn't show :00", {
          start: "1982-05-25T05:00",
          end: "1982-05-25T07:00",
          result: "May 25, 1982, 5 - 7 AM"
        });
        return test("mixed times still shows :30", {
          start: "1982-05-25T05:00",
          end: "1982-05-25T05:30",
          result: "May 25, 1982, 5 - 5:30 AM"
        });
      });
      describe("implicit minutes", function() {
        return test("still shows the :00", {
          start: thisYear("05-25", "05:00"),
          end: thisYear("05-25", "07:00"),
          options: {
            implicitMinutes: false
          },
          result: "May 25, 5:00 - 7:00 AM"
        });
      });
      describe("all day ranges", function() {
        test("one day has no range", {
          start: "2010-08-25",
          end: "2010-08-25",
          allDay: true,
          result: "Aug 25, 2010"
        });
        test("same month says month on one side", {
          start: thisYear("05-25"),
          end: thisYear("05-26"),
          allDay: true,
          result: "May 25 - 26"
        });
        test("same month says month on one side, with year if requested", {
          start: thisYear("05-25"),
          end: thisYear("05-26"),
          allDay: true,
          options: {
            implicitYear: false
          },
          result: "May 25 - 26, " + ((new Date).getFullYear())
        });
        test("different month shows both", {
          start: thisYear("05-25"),
          end: thisYear("06-01"),
          allDay: true,
          result: "May 25 - Jun 1"
        });
        test("different month shows both, with year if requested", {
          start: thisYear("05-25"),
          end: thisYear("06-01"),
          allDay: true,
          options: {
            implicitYear: false
          },
          result: "May 25 - Jun 1, " + ((new Date).getFullYear())
        });
        test("explicit year shows the year once", {
          start: "1982-05-25",
          end: "1982-05-26",
          allDay: true,
          result: "May 25 - 26, 1982"
        });
        test("different year shows the year twice", {
          start: "1982-05-25",
          end: "1983-05-25",
          allDay: true,
          result: "May 25, 1982 - May 25, 1983"
        });
        test("different year different month shows the month at the end", {
          start: "1982-05-25",
          end: "1983-06-01",
          allDay: true,
          result: "May 25, 1982 - Jun 1, 1983"
        });
        return test("explicit allDay", {
          start: "1982-05-25",
          end: "1982-05-25",
          allDay: true,
          options: {
            explicitAllDay: true
          },
          result: "all day May 25, 1982"
        });
      });
      describe("no single dates", function() {
        test("shouldn't show dates for intraday", {
          start: "2010-05-25 05:30",
          end: "2010-05-25 06:30",
          options: {
            showDate: false
          },
          result: "5:30 - 6:30 AM"
        });
        test("should show the dates for multiday", {
          start: thisYear("05-25", "05:30"),
          end: thisYear("05-27", "06:30"),
          options: {
            showDate: false
          },
          result: "May 25, 5:30 AM - May 27, 6:30 AM"
        });
        return test("should just say 'all day' for all day rangess", {
          start: thisYear("05-25"),
          end: thisYear("05-25"),
          options: {
            showDate: false
          },
          allDay: true,
          result: "all day"
        });
      });
      describe("ungroup meridiems", function() {
        test("should put meridiems on both sides", {
          start: thisYear("05-25", "05:30"),
          end: thisYear("05-25", "07:30"),
          options: {
            groupMeridiems: false
          },
          result: "May 25, 5:30 AM - 7:30 AM"
        });
        return test("even with abbreviated hours", {
          start: thisYear("05-25", "19:00"),
          end: thisYear("05-25", "21:00"),
          options: {
            groupMeridiems: false
          },
          result: "May 25, 7 PM - 9 PM"
        });
      });
      describe("no meridiem spaces", function() {
        return test("should skip the meridiem space", {
          start: thisYear("05-25", "05:30"),
          end: thisYear("05-25", "07:30"),
          options: {
            spaceBeforeMeridiem: false,
            groupMeridiems: false
          },
          result: "May 25, 5:30AM - 7:30AM"
        });
      });
      describe("24 hours", function() {
        test("shouldn't show meridians", {
          start: thisYear("05-25", "05:30"),
          end: thisYear("05-25", "19:30"),
          options: {
            twentyFourHour: true
          },
          result: "May 25, 5:30 - 19:30"
        });
        return test("always shows the :00", {
          start: thisYear("05-25", "12:00"),
          end: thisYear("05-25", "15:00"),
          options: {
            twentyFourHour: true
          },
          result: "May 25, 12:00 - 15:00"
        });
      });
      describe("show day of week", function() {
        test("should show day of week", {
          start: "2013-05-25T05:30",
          end: "2013-05-28T19:30",
          options: {
            showDayOfWeek: true
          },
          result: "Sat May 25, 5:30 AM - Tue May 28, 7:30 PM, 2013"
        });
        test("should show day of week, specify day of week format", {
          start: "2013-08-25T05:30",
          end: "2013-08-28T19:30",
          options: {
            showDayOfWeek: true,
            weekdayFormat: "dddd"
          },
          result: "Sunday Aug 25, 5:30 AM - Wednesday Aug 28, 7:30 PM, 2013"
        });
        test("collapses show day of week", {
          start: "2013-05-25T05:30",
          end: "2013-05-25T19:30",
          options: {
            showDayOfWeek: true
          },
          result: "Sat May 25, 2013, 5:30 AM - 7:30 PM"
        });
        return test("doesn't collapse with one week of separation", {
          start: "2013-05-25",
          end: "2013-06-01",
          allDay: true,
          options: {
            showDayOfWeek: true
          },
          result: "Sat May 25 - Sat Jun 1, 2013"
        });
      });
      return describe("goes into the morning", function() {
        test("elides late nights", {
          start: "1982-05-25 17:00",
          end: "1982-05-26 02:00",
          options: {
            lastNightEndsAt: 5
          },
          result: "May 25, 1982, 5 PM - 2 AM"
        });
        test("keeps late mornings", {
          start: "1982-05-25 17:00",
          end: "1982-05-26 10:00",
          options: {
            lastNightEndsAt: 5
          },
          result: "May 25, 5 PM - May 26, 10 AM, 1982"
        });
        test("morning start is adjustable", {
          start: "1982-05-25 17:00",
          end: "1982-05-26 10:00",
          options: {
            lastNightEndsAt: 11
          },
          result: "May 25, 1982, 5 PM - 10 AM"
        });
        test("doesn't elide if you start in the AM", {
          start: "1982-05-25 05:00",
          end: "1982-05-26 04:00",
          options: {
            lastNightEndsAt: 5
          },
          result: "May 25, 5 AM - May 26, 4 AM, 1982"
        });
        describe("and we're trying to hide the date", function() {
          test("elides the date too for early mornings", {
            start: "1982-05-25 17:00",
            end: "1982-05-26 02:00",
            options: {
              lastNightEndsAt: 5,
              showDate: false
            },
            result: "5 PM - 2 AM"
          });
          return test("doesn't elide if the morning ends late", {
            start: "1982-05-25 17:00",
            end: "1982-05-26 10:00",
            options: {
              lastNightEndsAt: 5
            },
            result: "May 25, 5 PM - May 26, 10 AM, 1982"
          });
        });
        return describe("other options", function() {
          return it("accepts a custom format", function() {
            return {
              start: "1982-05-25 17:00",
              end: "1982-05-26 10:00",
              options: {
                template: function(first, second) {
                  return "" + first + " | " + second;
                }
              },
              result: "May 25, 5 PM | May 26, 10 AM, 1982"
            };
          });
        });
      });
    });
    return describe("internationalization", function() {
      it("uses alternative language when specified by moment", function() {
        var range, start;
        start = moment("1982-05-25").lang("fr");
        range = start.twix(start.clone().add(1, 'days'));
        return assertEqual('25 mai, 0:00 - 26 mai, 0:00, 1982', range.format());
      });
      return it("uses English formatting rules when there's no format for the specified language", function() {
        var range, start;
        start = moment("1982-10-14").lang("de");
        range = start.twix(start.clone().add(1, 'days'));
        return assertEqual('Okt. 14, 12 AM - Okt. 15, 12 AM, 1982', range.format());
      });
    });
  };

  if (typeof define !== "undefined" && define !== null) {
    define(["moment", "twix"], function(moment, Twix) {
      return test(moment, Twix);
    });
  } else {
    moment = (_ref = typeof require === "function" ? require("moment") : void 0) != null ? _ref : this.moment;
    Twix = (_ref1 = typeof require === "function" ? require("../../bin/twix") : void 0) != null ? _ref1 : this.Twix;
    test(moment, Twix);
  }

}).call(this);
</body></html>