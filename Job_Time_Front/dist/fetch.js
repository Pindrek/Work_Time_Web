export async function Post_func() {
    await fetch("http://localhost:8000/core/home/", {
        method: "POST",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
            progress: "P0DT00H00M00S",
            progress_bar: 0,
        })
    });
}
export async function Patch_func(progress_, progress_bar_) {
    await fetch("http://localhost:8000/core/home/", {
        method: "PATCH",
        headers: { "content-type": "application/json" },
        body: JSON.stringify({
            progress: progress_,
            progress_bar: progress_bar_,
        })
    });
}
export async function Get_func() {
    const response = await fetch("http://localhost:8000/core/home/", {
        method: "GET",
    });
    const data = await response.json();
    return data;
}
//# sourceMappingURL=fetch.js.map