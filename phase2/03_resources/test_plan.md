| Initial State | Event | Next State | 
|-|-|-|
| No Allowlist or droplist | Invalid doc updater | Error for lack of files |
| Both Allowlist or droplist | Invalid doc updater | Error since both files are present |
| Only Allowlist | Doc updater | Docs from origianls in allowlist go to finals folder all others not specified get left |
| Only Droplist | Doc updater | Docs from origianls in droplist get left in originals and the rest go to finals folder |
| Allowlist + updates | Doc updater | All updates moved across to final, and any files in allowlist from originals that arent in updates|
| Droplist + updates | Doc updater | All updates moved across to final, and any files in droplist from originals that arent in updates are removed|

Tests to run
 1. Check all errors are displaying correctly
    - Program run without specifying a directory on which to operate
        - Fine
    - "originals" folder not found
        - Fine
    - "updates" folder not found
        - Fine
    - Missing both droplist and allowlist
        - Fine
    - Both droplist and allowlist are specified
        - Fine
    - Document(s) don't contain correctly formatted addresses
        - 6 lines raises error properly
        - 3 lines raises error properly
 2. Allowlist allows all with only one to update
    - Should have all files in final with the single updated
    - Real: only the updated file was in the finals folder
 3. Droplist removes all specified even if in update
    - Should remove all files in droplist and add update files
    - Real: the update file makes it across
    - Correct
 4. Allowlist no updates
    - Should only move allwed files
    - Real: It correctly moves the files across
 5. Droplist no updats
    - Should allow non-specified files
    - Real: It correctly dropped specified files and moved the rest

# Bug report

## Description

Update files superseed allowlist even when files are not specified in updates but are in allowlist

## Steps to reproduce

1. Have more than 1 files in the originals folder
2. Have 1 file to be updated in the updates folder
3. Add all other files to the allowlist
4. Run the document updater program
5. In finals you will see only the updated file and none of the files from the allowlist

## Defect management rating

High - This can lead to a loss of important data due to the update folder only being transfered





