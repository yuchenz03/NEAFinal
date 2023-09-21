function deleteGoal(goalID) {
    fetch("/delete-goal", {
      method: "POST",
      body: JSON.stringify({ goalID: goalID }),
    }).then((_res) => {
      window.location.href = "/swimmerGoals";
    });
  }

function deleteTime(timeID) {
    fetch("/delete-time", {
      method: "POST",
      body: JSON.stringify({ timeID: timeID }),
    }).then((_res) => {
      window.location.href = "/swimmerPBs";
    });
  }

function deleteEntry(entryID) {
    fetch("/delete-entry", {
      method: "POST",
      body: JSON.stringify({ timeID: entryID }),
    }).then((_res) => {
      window.location.href = "/swimmerJournal";
    });
  }