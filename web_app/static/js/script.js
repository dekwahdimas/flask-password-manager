function deletePass(pass_dataId) {
    fetch("/delete-password", {
        method: "POST",
        body: JSON.stringify({
            pass_dataId: pass_dataId
        }),
    }).then((_res) => {
        window.location.href = "/manage";
    });
}