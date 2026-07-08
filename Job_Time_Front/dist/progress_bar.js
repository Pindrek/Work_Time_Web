import { Get_func } from "./fetch.js";
let progress_bar_value = 0;
let time = 0;
export async function addTime() {
    const data = await Get_func();
    progress_bar_value = data[0].progress_bar;
    let second = parseInt(data[0].progress.slice(10, 12), 10);
    let minute = parseInt(data[0].progress.slice(7, 9), 10);
    let hour = parseInt(data[0].progress.slice(4, 6), 10);
    time += (hour * 3600) + (minute * 60) + second;
    return time;
}
export function ProgressBar() {
    time++;
    if (progress_bar_value < 100 && time % 288 === 0)
        progress_bar_value++;
    return progress_bar_value;
}
//# sourceMappingURL=progress_bar.js.map