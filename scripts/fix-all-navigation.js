// Comprehensive Navigation Fixer - All Templates
const fs = require('fs');
const path = require('path');

const templatesDir = path.join(__dirname, '../templates');

function fixAllNavigation(content) {
  // Fix dropdown menu items with href="#"
  content = content.replace(
    /href="#"\s+class="dropdown-item">Wellness Programs/g,
    'href="/wellness" class="dropdown-item">Wellness Programs'
  );
  content = content.replace(
    /href="#"\s+class="dropdown-item">Therapy Programs/g,
    'href="/therapy" class="dropdown-item">Therapy Programs'
  );
  content = content.replace(
    /href="#"\s+class="dropdown-item">Women & Senior Programs/g,
    'href="/women-wellness" class="dropdown-item">Women & Senior Programs'
  );
  content = content.replace(
    /href="#"\s+class="dropdown-item">Professional Training/g,
    'href="/professional" class="dropdown-item">Professional Training'
  );
  content = content.replace(
    /href="#"\s+class="dropdown-item">Workshops/g,
    'href="/workshops" class="dropdown-item">Workshops'
  );
  
  // Fix mobile menu items
  content = content.replace(
    /href="#"\s+class="block text-white[^>]*>Wellness Programs/g,
    'href="/wellness" class="block text-white hover:text-green-500 px-3 py-2 rounded-md text-base font-medium transition duration-300">Wellness Programs'
  );
  content = content.replace(
    /href="#"\s+class="block text-white[^>]*>Therapy Programs/g,
    'href="/therapy" class="block text-white hover:text-green-500 px-3 py-2 rounded-md text-base font-medium transition duration-300">Therapy Programs'
  );
  content = content.replace(
    /href="#"\s+class="block text-white[^>]*>Women & Senior Programs/g,
    'href="/women-wellness" class="block text-white hover:text-green-500 px-3 py-2 rounded-md text-base font-medium transition duration-300">Women & Senior Programs'
  );
  content = content.replace(
    /href="#"\s+class="block text-white[^>]*>Professional Training/g,
    'href="/professional" class="block text-white hover:text-green-500 px-3 py-2 rounded-md text-base font-medium transition duration-300">Professional Training'
  );
  content = content.replace(
    /href="#"\s+class="block text-white[^>]*>Workshops/g,
    'href="/workshops" class="block text-white hover:text-green-500 px-3 py-2 rounded-md text-base font-medium transition duration-300">Workshops'
  );
  
  // Fix other common navigation items
  content = content.replace(/href="#"\s+class="[^"]*">Meet The Trainer/g, 'href="/meet-the-trainer" class="text-gray-700 hover:text-green-500 px-3 py-2 rounded-md text-sm font-medium transition duration-300">Meet The Trainer');
  content = content.replace(/href="#contact"/g, 'href="/contact"');
  
  return content;
}

function processAllTemplates() {
  const files = fs.readdirSync(templatesDir);
  let count = 0;
  
  files.forEach(file => {
    if (file.endsWith('.ejs')) {
      const filePath = path.join(templatesDir, file);
      let content = fs.readFileSync(filePath, 'utf8');
      const originalContent = content;
      
      content = fixAllNavigation(content);
      
      if (content !== originalContent) {
        fs.writeFileSync(filePath, content, 'utf8');
        console.log(`✅ Fixed navigation in: ${file}`);
        count++;
      }
    }
  });
  
  console.log(`\n✅ Fixed navigation in ${count} files!`);
}

if (require.main === module) {
  processAllTemplates();
}

module.exports = { fixAllNavigation, processAllTemplates };
