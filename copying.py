import shutil

# Copy src to dst. (cp src dst)
shutil.copy(src, dst)

#Copy files, but preserve metadata (cp -p src dst)

shutil.copy2(src, dst)

#Copy directory tree (cp -R src dst)

shutil.copytree(src, dst)

#Move src tpo dst (mv src dst)
shutil.move(src, dst)
