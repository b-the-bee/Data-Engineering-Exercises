

# my_food = "cereal"
# ./print_my_food.sh

# set -eu

# echo -n "Enter some text: "
# read var

# if [[ $var == "splab" ]]
# then
#     echo "The variable is splab."
# fi

if [[ -s "$1" ]]; then
    echo "$1 exists!"
else
    echo "$1 does not exist or is empty"
fi