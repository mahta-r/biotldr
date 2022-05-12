#!/bin/bash
python to_stories.py $TASK
python make_datafiles.py --stories_dir $TASK/stories --urldir $TASK/mapping --finished_files_dir $TASK

# Make dataset with crl tags
python build_ctrl_datasets.py $TASK

python to_stories.py $TASK/ctrl
python make_datafiles.py --stories_dir $TASK/ctrl/stories --urldir $TASK/ctrl/mapping --finished_files_dir $TASK/ctrl
