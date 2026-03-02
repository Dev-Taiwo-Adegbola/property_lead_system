document.addEventListener("DOMContentLoaded", function () {

    // WhatsApp integration
    const BasewhatsappBtn = document.querySelectorAll('.whatsapp')
    const BaseWhatsAppMessage = 'Hello! I found your Website and i am interested in your Properties'
    const PropertyWhatsAppMessage = ''
    BasewhatsappBtn.forEach((e)=>{
        e.onclick = ()=>{
        
        document.location.href = `https://wa.me/+2349049760979?text=${encodeURIComponent(
    BaseWhatsAppMessage
  )}`;

    }
    })

    // NAVIGATION
  const navigationButton = document.querySelector("#nav-button");
  const navigationMenu = document.querySelector(".navMenu");
  const closeButton = document.querySelector("#close-nav");  

    navigationButton.addEventListener("click",  () => {
        if (navigationMenu.classList.contains("max-lg:-translate-x-[120%]")) {
            navigationMenu.classList.toggle("max-lg:-translate-x-[120%]");
            navigationMenu.classList.toggle("max-lg:translate-x-0");
        } else {
            navigationMenu.classList.toggle("max-lg:translate-x-0");
            navigationMenu.classList.toggle("max-lg:-translate-x-[120%]");
        } 
})

closeButton.addEventListener("click",  () => {
    if (navigationMenu.classList.contains("max-lg:-translate-x-[120%]")) {
        navigationMenu.classList.toggle("max-lg:-translate-x-[120%]");
        navigationMenu.classList.toggle("max-lg:translate-x-0");
    } else {
        navigationMenu.classList.toggle("max-lg:translate-x-0");
        navigationMenu.classList.toggle("max-lg:-translate-x-[120%]");
    }})

    

    // FOOTER

    const currentYear = new Date().getFullYear();
    const footer = document.querySelector("footer #footer-year");
    footer.textContent = `© ${currentYear} PrimeNest Realty. All rights reserved.`;
});
