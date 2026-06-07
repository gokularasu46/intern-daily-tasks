document.addEventListener("DOMContentLoaded", () => {
    const hamburger = document.querySelector(".hamburger");
    const navMenu = document.querySelector(".nav-menu");
    const navLinks = document.querySelectorAll(".nav-link");
    const sections = document.querySelectorAll("main section[id]");
    const contactForm = document.querySelector("#contactForm");

    const closeMenu = () => {
        navMenu?.classList.remove("active");
        hamburger?.classList.remove("active");
        hamburger?.setAttribute("aria-expanded", "false");
    };

    hamburger?.addEventListener("click", () => {
        const isOpen = navMenu.classList.toggle("active");
        hamburger.classList.toggle("active", isOpen);
        hamburger.setAttribute("aria-expanded", String(isOpen));
    });

    navLinks.forEach((link) => {
        link.addEventListener("click", (event) => {
            const targetId = link.getAttribute("href");
            if (!targetId || !targetId.startsWith("#")) return;

            const target = document.querySelector(targetId);
            if (!target) return;

            event.preventDefault();
            closeMenu();
            target.scrollIntoView({ behavior: "smooth", block: "start" });
        });
    });

    document.addEventListener("click", (event) => {
        if (!event.target.closest(".navbar")) {
            closeMenu();
        }
    });

    const navObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (!entry.isIntersecting) return;
                navLinks.forEach((link) => {
                    link.classList.toggle("active", link.getAttribute("href") === `#${entry.target.id}`);
                });
            });
        },
        { rootMargin: "-35% 0px -55% 0px", threshold: 0 }
    );

    sections.forEach((section) => navObserver.observe(section));

    const revealObserver = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    revealObserver.unobserve(entry.target);
                }
            });
        },
        { threshold: 0.12 }
    );

    document.querySelectorAll(".section-animate").forEach((item) => revealObserver.observe(item));

    contactForm?.addEventListener("submit", (event) => {
        event.preventDefault();
        alert("Thank you. Your message has been recorded for demo purposes.");
        contactForm.reset();
    });
});
