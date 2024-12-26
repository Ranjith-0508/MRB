

document.addEventListener("DOMContentLoaded", function () {
    const progressBars = document.querySelectorAll(".progress");
    progressBars.forEach(bar => {
        const progress = bar.getAttribute("data-progress");
        bar.style.width = progress;
    });
});
document.querySelectorAll('.faq-item h3').forEach(item => {
    item.addEventListener('click', () => {
        item.parentElement.classList.toggle('active');
    });
});

