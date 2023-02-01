| Website | Description | WAVE report | Lighthouse report | colorblindly |
| ------- | ----------- | ----------- | ----------------- | ------------ |
| https://www.hotukdeals.com/ | hotukdeals | 64 errors - missing alt text, missing form labels, empyty buttons, contrast errors | 65 - Buttons do not have accesible names, images don't have alt text, links do not have discernable names, colour contrast is not | Relatively good |
| https://www.bbc.co.uk/sport/football | BBC sport football | 8 errors - empty links, empty table headers, contrast errors | 83 - aria ids are not unique, links do not have a discernable name, headings not in sequentially descding order | Relatively good |
| https://www.asos.com/men/ | ASOS | 10 errors - missing alt text, empty labels, buttons and heading, broken aria reference, some contrast errors | 82 - attributes do not match their roles, buttons and links do not have accesible names| Some buttons blend in to background on some color blind settings |
| https://www.costco.co.uk/ | Costco | 46 errors - missing alt text, empty buttons, broken aria reference and aria menu | 73 - aria attributes do not match role and id's are not unique, buttons and links do not have accesible names, missing alt text | Relatively okay |
| https://www.w3.org/WAI/demos/bad/before/home.html | Accesibility website | 37 errors missing alt text, 0 errors | (Inaccesable 59), (Accesible 100)| Relatively okay |

## HOTUKDEALS
### Who might struggle to use this site?

- Visually impaired people due to the lack of alt text and link names as text to speech may have a hard time transcribing effectively
- Invisible elements which may be read out to users which cant be interacted with

### Which defects would you prioritise fixing?

- Fixing alt text for images, and providing discernable names for links

### Are the tools finding the same thing?

 - both found the same things
 - found invisible elements

## City Lights Site
1. What makes the inaccessible version of the site more difficult to use?
    - Random invisible elements.
    - Description of citylights logo is very long and detailed. Perhaps too much
    - Has ranmdom unlabelled image in the middle
    - Another unlabelled image - a .gif file with sun a cloud
    - Random containers
    - Home, news, survey buttons are not labelled correctly
    - Tickets is read as nav_facts.
    - 'C' on news heather is unlabelled
    - Images in article have no label - exist in empty group
    - Links in articles have no label
    - Phone number is an image and labelled with the wrong number.
    - Images on side articles also not labeled.
2. Could you have predicted the outcome based on the appearance of each version?
    - No they look relatively the same
3. Did you notice any defects that were not identified by WAVE/Lighthouse?
    - The grouping of elements on the page meant it repeated a lot of text not user friendly
4. What are the differences and similarities between “accessibility testing” and “usability testing”?
    - Better image description
    - Things are not in groups
    - Sidebar items are adequately labelled
    - For middle articles, voiceover does not read image or 'C'
    - Links have adequate labels and description