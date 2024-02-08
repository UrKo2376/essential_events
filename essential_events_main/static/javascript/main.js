// Begin responmsive menu JS
function showSidebar() {
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'flex'
}

function hideSidebar() {
    const sidebar = document.querySelector('.sidebar')
    sidebar.style.display = 'none'
}

// End responmsive menu JS

// Begin Grayscale JS
document.addEventListener('DOMContentLoaded', function() {
    // Get all elements with the 'grayscale' class
    const heroItems = document.querySelectorAll('.grayscale');

    // Loop through each element
    heroItems.forEach(function(item) {
        // Add event listeners for mouseover and mouseout
        item.addEventListener('mouseover', function() {
            // Remove the grayscale filter on mouseover
            item.style.filter = 'grayscale(0%)';
        });

        item.addEventListener('mouseout', function() {
            // Add the grayscale filter on mouseout
            item.style.filter = 'grayscale(100%)';
        });
    });
});
// End Grayscale JS