import { Patch_func } from "./fetch.js";
import { ProgressBar } from "./progress_bar.js";
import { Get_func } from "./fetch.js";
import { DrawTable } from "./table.js";
import { addTime } from "./progress_bar.js";
import { DrawStat } from "./statistic.js";
import { Post_func } from "./fetch.js";
await Post_func();
await addTime();
void DrawTable();
DrawStat();
const data = await Get_func();
let seconds = parseInt(data[0].progress.slice(10, 12), 10);
let minutes = parseInt(data[0].progress.slice(7, 9), 10);
let hours = parseInt(data[0].progress.slice(4, 6), 10);
let timer = null;
function startTimer() {
    timer = window.setInterval(() => {
        seconds++;
        if (seconds === 60) {
            minutes++;
            seconds = 0;
        }
        if (minutes === 60) {
            hours++;
            minutes = 0;
        }
        void DrawTable();
        Patch_func(timeToProgress(), ProgressBar());
    }, 1000);
}
export function timeToProgress() {
    return `P0DT${hours}H${minutes}M${seconds}S`;
}
const startButton = document.getElementById("start");
const stopButton = document.getElementById("stop");
startButton?.addEventListener("click", () => {
    console.log("Start");
    if (timer === null) {
        startTimer();
    }
});
stopButton?.addEventListener("click", () => {
    console.log("stop");
    if (timer !== null) {
        clearInterval(timer);
        timer = null;
    }
});
setInterval(() => {
    DrawStat();
}, 60000);
//# sourceMappingURL=progress.js.map