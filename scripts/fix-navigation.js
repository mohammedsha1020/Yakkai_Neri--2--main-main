// Script to fix all navigation links in EJS templates
const fs = require('fs');
const path = require('path');

const templatesDir = path.join(__dirname, '../templates');

// Mapping of old .html links to new Express routes
const linkReplacements = {
  'wellness.html': '/wellness',
  'therapy.html': '/therapy',
  'professional.html': '/professional',
  'workshops.html': '/workshops',
  'courses.html': '/courses',
  'contact.html': '/contact',
  'meet-the-trainer.html': '/meet-the-trainer',
  'corporate-yoga.html': '/corporate-yoga',
  'women-wellness.html': '/women-wellness',
  'women-seniors.html': '/women-seniors',
  'yoga-as-sport.html': '/yoga-as-sport',
  'yoga-for-sport.html': '/yoga-for-sport',
  'adolescence.html': '/adolescence',
  'prenatal-postnatal.html': '/prenatal-postnatal',
  'tech-supported-yoga.html': '/tech-supported-yoga',
  'index.html': '/',
  'admin.html': '/admin'
};

function fixNavigationLinks(content) {
  let modified = content;
  
  // Replace all .html links with proper routes
  Object.entries(linkReplacements).forEach(([oldLink, newLink]) => {
    // Match href="filename.html" and href="./filename.html"
    const regex1 = new RegExp(`href=["'](?:\\./)?(${oldLink.replace('.', '\\.')})["']`, 'g');
    modified = modified.replace(regex1, `href="${newLink}"`);
  });
  
  // Fix # links to actual routes for dropdown items
  modified = modified.replace(/href="#" class="dropdown-item">Wellness Programs/g, 
    'href="/wellness" class="dropdown-item">Wellness Programs');
  modified = modified.replace(/href="#" class="dropdown-item">Therapy Programs/g, 
    'href="/therapy" class="dropdown-item">Therapy Programs');
  modified = modified.replace(/href="#" class="dropdown-item">Professional Training/g, 
    'href="/professional" class="dropdown-item">Professional Training');
    
  // Fix mobile menu links
  modified = modified.replace(/href="#" class="block text-white hover:text-green-500[^>]+>Wellness Programs/g, 
    'href="/wellness" class="block text-white hover:text-green-500 px-3 py-2 rounded-md text-base font-medium transition duration-300">Wellness Programs');
  modified = modified.replace(/href="#" class="block text-white hover:text-green-500[^>]+>Therapy Programs/g, 
    'href="/therapy" class="block text-white hover:text-green-500 px-3 py-2 rounded-md text-base font-medium transition duration-300">Therapy Programs');
  modified = modified.replace(/href="#" class="block text-white hover:text-green-500[^>]+>Professional Training/g, 
    'href="/professional" class="block text-white hover:text-green-500 px-3 py-2 rounded-md text-base font-medium transition duration-300">Professional Training');
  
  return modified;
}

function processAllTemplates() {
  const files = fs.readdirSync(templatesDir);
  let count = 0;
  
  files.forEach(file => {
    if (file.endsWith('.ejs')) {
      const filePath = path.join(templatesDir, file);
      let content = fs.readFileSync(filePath, 'utf8');
      const originalContent = content;
      
      content = fixNavigationLinks(content);
      
      if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ Fixed navigation links in: ${file}`);
        count++;
      }
    }
  });
  
  console.log(`\n✅ Fixed navigation links in ${count} files!`);
}

if (require.main === module) {
  processAllTemplates();
}

module.exports = { fixNavigationLinks, processAllTemplates };
